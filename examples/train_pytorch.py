import os
import torch
import random
import medsegbench
import numpy as np
from medsegbench import INFO
import torch.optim as optim
import torch.utils.data as data
import segmentation_models_pytorch as smp
import torchvision.transforms as transforms
from medsegbench.checkpoint import BestModelCheckPoint
import matplotlib.pyplot as plt
def seed_torch(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True

def main(dataset_list):

    path = "results" #Should be in main directory
    for data_flag in dataset_list:
        
        # Dataset info
        info = INFO[data_flag]
        task = info['task']
        n_channels = info['n_channels_im']
        n_classes = len(info['pixel_labels'])
        n_samples = info['n_samples']
        min_sample_count = min([n_samples['train'], n_samples['val']])

        # Parameters
        NBR_EPOCH = 200
        BATCH_SIZE = 16
        while BATCH_SIZE > min_sample_count:
            BATCH_SIZE = BATCH_SIZE // 2
        print("BATCH SIZE:", BATCH_SIZE)

        for ENCODER_NAME in ['resnet18', 'resnet50', 'efficientnet-b0','mobilenet_v2', 'densenet121', 'mit_b0']:
            
            if ENCODER_NAME == 'mit_b0' and n_channels != 3:
                continue

            # Directory exist?
            if not os.path.exists(f"{path}/{data_flag}/{ENCODER_NAME}"):
                os.makedirs(f"{path}/{data_flag}/{ENCODER_NAME}")

            for seed in [0, 42, 3074]:
                
                seed_torch(seed)
                print("DATASET:", data_flag, "ENCODER:", ENCODER_NAME, "SEED:", seed)
                
                log = ""
                download = False

                DataClass = getattr(medsegbench, info['python_class'])
                checkpoint = BestModelCheckPoint(ENCODER_NAME)

                # preprocessing
                data_transform = transforms.Compose([
                    transforms.ToTensor()
                ])

                # load the data
                train_dataset = DataClass(split='train', transform=data_transform, target_transform = data_transform, download=download)
                val_dataset = DataClass(split='val', transform=data_transform, target_transform = data_transform, download=download)
                
                # encapsulate data into dataloader form
                train_loader = data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
                val_loader = data.DataLoader(dataset=val_dataset, batch_size=BATCH_SIZE, shuffle=True)
                
                device = torch.device('cuda')

                model = smp.Unet(
                    encoder_name=ENCODER_NAME,        # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
                    encoder_weights=None,     # use `imagenet` pre-trained weights for encoder initialization
                    in_channels=n_channels,                  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
                    classes=1,                      # model output channels (number of classes in your dataset)
                )

                model.to(device)
                optimizer = optim.Adam(model.parameters(), lr=1e-3) # 1e-3
                # for image segmentation dice loss could be the best first choice
                loss_fn = smp.losses.DiceLoss(smp.losses.BINARY_MODE, from_logits=True)

                for epoch in range(NBR_EPOCH):

                    train_loss = []
                    train_iou = []
                    model.train()
                    for inputs, labels in train_loader:
                        inputs, labels = inputs.to(device), labels.to(device)
                        
                        with torch.set_grad_enabled(True):
                            logits_mask = model(inputs)
                            loss = loss_fn(logits_mask, labels)
                            train_loss.append(loss.item())
                            
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

                            # dataset IoU means that we aggregate intersection and union over whole dataset
                            # and then compute IoU score. The difference between dataset_iou and per_image_iou scores
                            # in this particular case will not be much, however for dataset 
                            # with "empty" images (images without target class) a large gap could be observed. 
                            # Empty images influence a lot on per_image_iou and much less on dataset_iou.
                            dataset_iou = smp.metrics.iou_score(tp, fp, fn, tn, reduction="micro")
                            
                            train_iou.append(dataset_iou)

                            optimizer.zero_grad()
                            loss.backward()
                            optimizer.step()

                        del logits_mask
                        del loss
                        del inputs
                        del labels
                    
                    # Validation Phase
                    val_loss = []
                    val_iou = []
                    model.eval()
                    for inputs, labels in val_loader:
                        inputs, labels = inputs.to(device), labels.to(device)
                        with torch.set_grad_enabled(False):
                            logits_mask = model(inputs)
                            loss = loss_fn(logits_mask, labels)
                            val_loss.append(loss.item())
                            
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

                            # dataset IoU means that we aggregate intersection and union over whole dataset
                            # and then compute IoU score. The difference between dataset_iou and per_image_iou scores
                            # in this particular case will not be much, however for dataset 
                            # with "empty" images (images without target class) a large gap could be observed. 
                            # Empty images influence a lot on per_image_iou and much less on dataset_iou.
                            dataset_iou = smp.metrics.iou_score(tp, fp, fn, tn, reduction="micro")
                            val_iou.append(dataset_iou)

                        del logits_mask
                        del loss
                        del inputs
                        del labels

                    avg_tr_loss = sum(train_loss) / len(train_loss)
                    avg_tr_score = sum(train_iou) / len(train_iou)
                    avg_val_loss = sum(val_loss) / len(val_loss)
                    avg_val_score = sum(val_iou) / len(val_iou)
                    txt = f"\nEpoch: {epoch}, tr_loss: {avg_tr_loss}, tr_f1_score: {avg_tr_score}, val_loss: {avg_val_loss}, val_iou: {avg_val_score}"
                    log += txt
                    print(txt)
                    checkpoint.check(avg_val_score, model, seed, data_flag)

                # Write Log
                with open(f"{path}/{data_flag}/{ENCODER_NAME}/log_{ENCODER_NAME}_seed_{seed}.txt", "w") as f:
                    f.write(log)

                torch.cuda.empty_cache()

## Main
if __name__ == '__main__':
    #dataset_list = ["covid19radio", "covidquex", "cystoidfluid", ]
    # dataset_list = ["cystoidfluid"]
    # dataset_list = ["pandental","nuclei"]
    dataset_list = ["nuclei"]
    main(dataset_list)
