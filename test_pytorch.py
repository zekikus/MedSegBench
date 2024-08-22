import os
import torch
import random
import medsegbench
import numpy as np
import pandas as pd
from medsegbench import INFO
import torch.utils.data as data
import segmentation_models_pytorch as smp
import torchvision.transforms as transforms

def seed_torch(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True

def main(dataset_list):

    result_df = pd.DataFrame(columns=["DATASET", "ENCODER_NAME", "SEED", "F1", "PREC", "REC", "ACC", "IOU"])
    for data_flag in dataset_list:
        
        # Dataset info
        info = INFO[data_flag]
        n_channels = info['n_channels_im']

        # Parameters
        BATCH_SIZE = 1
        print("BATCH SIZE:", BATCH_SIZE)

        for ENCODER_NAME in ['resnet18', 'resnet50',
                            'efficientnet-b0', 'mobilenet_v2', 'mit_b0', 'densenet121']:
            
            if ENCODER_NAME == 'mit_b0' and n_channels != 3:
                continue

            for seed in [0, 42, 3074]:
                
                seed_torch(seed)
                print("DATASET:", data_flag, "ENCODER:", ENCODER_NAME, "SEED:", seed)
                
                download = False
                DataClass = getattr(medsegbench, info['python_class'])

                # preprocessing
                data_transform = transforms.Compose([
                    transforms.ToTensor()
                ])

                # load the data
                test_dataset = DataClass(split='test', transform=data_transform, target_transform = data_transform, download=download)

                # encapsulate data into dataloader form
                test_loader = data.DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE, shuffle=False)

                device = torch.device('cuda')

                model = smp.Unet(
                    encoder_name=ENCODER_NAME,        # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
                    encoder_weights=None,     # use `imagenet` pre-trained weights for encoder initialization
                    in_channels=n_channels,                  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
                    classes=1,                      # model output channels (number of classes in your dataset)
                )

                model.load_state_dict(torch.load(f"results/{data_flag}/{ENCODER_NAME}/model_{ENCODER_NAME}_seed_{seed}.pt"))
                model.to(device)
                                    
                # Test Phase
                test_scores = {"F1": [], "PREC": [], "REC": [], "ACC": [], "IOU": []}
                model.eval()
                for inputs, labels in test_loader:
                    inputs, labels = inputs.to(device), labels.to(device)
                    with torch.no_grad():
                        logits_mask = model(inputs)
                        
                        # Lets compute metrics for some threshold
                        # first convert mask values to probabilities, then 
                        # apply thresholding
                        prob_mask = logits_mask.sigmoid()
                        pred_mask = (prob_mask > 0.5).float()

                        # We will compute IoU metric by two ways
                        #   1. dataset-wise
                        #   2. image-wise
                        # but for now we just compute true positive, false positive, false negative and
                        # true negative 'pixels' for each image and class
                        # these values will be aggregated in the end of an epoch
                        tp, fp, fn, tn = smp.metrics.get_stats(pred_mask.long(), labels.long(), mode="binary")

                        # per image IoU means that we first calculate IoU score for each image 
                        # and then compute mean over these scores
                        test_scores["IOU"].append(smp.metrics.iou_score(tp, fp, fn, tn, reduction="micro").item())
                        test_scores["F1"].append(smp.metrics.f1_score(tp, fp, fn, tn, reduction="micro").item())
                        test_scores["ACC"].append(smp.metrics.accuracy(tp, fp, fn, tn, reduction="micro").item())
                        test_scores["PREC"].append(smp.metrics.precision(tp, fp, fn, tn, reduction="micro").item())
                        test_scores["REC"].append(smp.metrics.recall(tp, fp, fn, tn, reduction="micro").item())

                    del logits_mask
                    del inputs
                    del labels

                # Data Frame
                new_row = dict()
                new_row.update({"DATASET": data_flag, "ENCODER_NAME": ENCODER_NAME, "SEED": seed})
                new_row.update({k: np.array(v)[~np.isnan(v)].mean() for k, v in test_scores.items()})
                result_df.loc[len(result_df.index)] = new_row

            torch.cuda.empty_cache()
    
        result_df.to_excel("results/all_result.xlsx")

## Main
if __name__ == '__main__':
    dataset_list = ["nuclei"]
    main(dataset_list)
