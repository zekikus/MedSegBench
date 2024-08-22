import os
from torch import from_numpy
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from medsegbench.info import INFO, HOMEPAGE, DEFAULT_ROOT

class MedSegBench(Dataset):

    flag = ...

    def __init__(self,
                 split,
                 transform = None,
                 target_transform = None,
                 download = False,
                 as_rgb = False,
                 root = DEFAULT_ROOT,
                 size=512,
                 category = None,
                 mmap_mode=None,
                ):
        
        """
        Args:

            split (string): 'train', 'val' or 'test', required
            transform (callable, optional): A function/transform that takes in an PIL image and returns a transformed version. Default: None.
            target_transform (callable, optional): A function/transform that takes in the target and transforms it. Default: None.
            download (bool, optional): If true, downloads the dataset from the internet and puts it in root directory. If dataset is already downloaded, it is not downloaded again. Default: False.
            as_rgb (bool, optional): If true, convert grayscale images to 3-channel images. Default: False.
            size (int, optional): The size of the returned images. If None, use MNIST-like 28. Default: None.
            mmap_mode (str, optional): If not None, read image arrays from the disk directly. This is useful to set `mmap_mode='r'` to save memory usage when the dataset is large (e.g., PathMNIST-224). Default: None.
            root (string, optional): Root directory of dataset. Default: `~/.medsegbench`.
        """

        self.size = size
        self.category = category
        self.size_flag = f"_{size}"
        self.info = INFO[self.flag]

        if root is not None and os.path.exists(root):
            self.root = root
        else:
            raise RuntimeError(
                "Failed to setup the default `root` directory. "
                + "Please specify and create the `root` directory manually."
            )
        
        if download:
            self.download()
        
        if not os.path.exists(
            os.path.join(self.root, f"{self.flag}{self.size_flag}.npz")
        ):
            raise RuntimeError(
                f"Dataset not found. You can set 'download=True' to download it"
            )
        
        npz_file = np.load(
            os.path.join(self.root, f"{self.flag}{self.size_flag}.npz"),
            mmap_mode=mmap_mode,
        )

        self.split = split
        self.transform = transform
        self.target_transform = target_transform
        self.as_rgb = as_rgb

        if self.split in ["train", "val", "test"]:
            if self.flag == 'idrib':
                self.imgs = npz_file[f"{self.split}_images"]
            else:
                self.imgs = npz_file[f"{self.split}_images" if self.category is None else f"{self.split}_images_{self.category}"]
            self.labels = npz_file[f"{self.split}_label" if self.category is None else f"{self.split}_label_{self.category}"] 
        else:
            raise ValueError

    def __len__(self):
        assert self.info["n_samples"][self.split] == self.imgs.shape[0]
        return self.imgs.shape[0]
    
    def __getitem__(self, index):
        """
        return: (without transform/target_transofrm)
            img: PIL.Image
            target: np.array of `L` (L=1 for single-label)
        """

        img, target = self.imgs[index], self.labels[index]
        if self.info['task'] == 'binary': target = target * 255
        img = Image.fromarray(img)

        if self.as_rgb:
            img = img.convert("RGB")

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            if self.info['task'] == 'binary':
                target = self.target_transform(target)
            else:
                target = from_numpy(target).unsqueeze(0)

        return img, target

    def download(self):
        try:
            from torchvision.datasets.utils import download_url

            download_url(
                url = self.info[f"url{self.size_flag}"],
                root = self.root,
                filename = f"{self.flag}{self.size_flag}.npz",
                md5 = self.info[f"MD5{self.size_flag}"],

            )
        except:
            raise RuntimeError(
                f"""
                Automatic download failed! Please download {self.flag}{self.size_flag}.npz manually.
                1. [Optional] Check your network connection: 
                    Go to {HOMEPAGE} and find the Zenodo repository
                2. Download the npz file from the Zenodo repository or its Zenodo data link: 
                    {self.info[f"url{self.size_flag}"]}
                3. [Optional] Verify the MD5: 
                    {self.info[f"MD5{self.size_flag}"]}
                4. Put the npz file under your MedSegBench root folder: 
                    {self.root}
                """
            )
    
    def montage(self, length=20, replace=False, save_folder=None, display_target = False, seed = None):
        from medsegbench.utils import montage2d

        if seed is not None:
            np.random.seed(seed)

        n_sel = length * length
        sel = np.random.choice(self.__len__(), size=n_sel, replace=replace)

        montage_img = montage2d(
            imgs=self.imgs if not display_target else self.labels, n_channels=self.info["n_channels_im"] if not display_target else self.info["n_channels_lbl"], sel=sel
        )

        if save_folder is not None:
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            montage_img.save(
                os.path.join(
                    save_folder, f"{self.flag}{self.size_flag}_{self.split}_montage.jpg"
                )
            )

        return montage_img
        
class KvasirMSBench(MedSegBench):
    flag = "kvasir"

class Isic2018MSBench(MedSegBench):
    flag = "isic2018"

class DriveMSBench(MedSegBench):
    flag = "drive"

class ChaseDB1MSBench(MedSegBench):
    flag = "chasedb1"

class Dca1MSBench(MedSegBench):
    flag = "dca1"

class ChuacMSBench(MedSegBench):
    flag = "chuac"

class WbcMSBench(MedSegBench):
    flag = "wbc"

class IdribMSBench(MedSegBench):
    flag = "idrib"

class CellnucleiMSBench(MedSegBench):
    flag = "cellnuclei"

class PandentalMSBench(MedSegBench):
    flag = "pandental"

class Bbbc010MSBench(MedSegBench):
    flag = "bbbc010"

class DynamicNuclearMSBench(MedSegBench):
    flag = "dynamicnuclear"

class NusetMSBench(MedSegBench):
    flag = "nuset"

class NucleiMSBench(MedSegBench):
    flag = "nuclei"

class TnbcnucleiMSBench(MedSegBench):
    flag = "tnbcnuclei"

class MonusacMSBench(MedSegBench):
    flag = "monusac"

class DeepbacsMSBench(MedSegBench):
    flag = "deepbacs"

class BriFiSegMSBench(MedSegBench):
    flag = "brifiseg"

class BusiMSBench(MedSegBench):
    flag = "busi"

class Covid19RadioMSBench(MedSegBench):
    flag = "covid19radio"

class CovidQUExMSBench(MedSegBench):
    flag = "covidquex"

class CystoFluidMSBench(MedSegBench):
    flag = "cystoidfluid"

class Isic2016MSBench(MedSegBench):
    flag = "isic2016"

class PolypGenMSBench(MedSegBench):
    flag = "polypgen"

class Promise12MSBench(MedSegBench):
    flag = "promise12"

class RoboToolMSBench(MedSegBench):
    flag = "robotool"

class UWSkinCancerMSBench(MedSegBench):
    flag = "uwaterlooskincancer"

class UltrasoundNerveMSBench(MedSegBench):
    flag = "ultrasoundnerve"

class USforKidneyMSBench(MedSegBench):
    flag = "usforkidney"

class YeazMSBench(MedSegBench):
    flag = "yeaz"

class BkaiIghMSBench(MedSegBench):
    flag = "bkai-igh"

class M2caiSegMSBench(MedSegBench):
    flag = "m2caiseg"

class AbdomenUSMSBench(MedSegBench):
    flag = "abdomenus"

class FHPsAOPMSBench(MedSegBench):
    flag = "fhpsaop"

class MosMedPlusMSBench(MedSegBench):
    flag = "mosmedplus"