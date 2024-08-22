import skimage
import numpy as np
from PIL import Image
from skimage.util import montage as skimage_montage

#====================================================================
# This part of the code is based on MedMNIST
# from https://github.com/MedMNIST/MedMNIST
# Yang, J., Shi, R., Wei, D., Liu, Z., Zhao, L., Ke, B., ... & Ni, B. (2023). Medmnist v2-a large-scale lightweight benchmark for 2d and 3d biomedical image classification. Scientific Data, 10(1), 41.
# ===================================================================

def montage2d(imgs, n_channels, sel):
    sel_img = imgs[sel]

    montage_arr = None

    # version 0.20.0 changes the kwarg `multichannel` to `channel_axis`
    if skimage.__version__ >= "0.20.0":
        montage_arr = skimage_montage(sel_img, channel_axis = 3 if len(sel_img.shape) == 4 else None)
    else:
        montage_arr = skimage_montage(sel_img, multichannel = (n_channels == 3))
    montage_img = Image.fromarray(montage_arr)

    return montage_img