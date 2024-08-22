import skimage
import numpy as np
from PIL import Image
from skimage.util import montage as skimage_montage

def montage2d(imgs, n_channels, sel):
    sel_img = imgs[sel]

    #if len(sel_img.shape) < 4:
     #   sel_img = np.expand_dims(sel_img, axis=-1)

    montage_arr = None

    # version 0.20.0 changes the kwarg `multichannel` to `channel_axis`
    if skimage.__version__ >= "0.20.0":
        montage_arr = skimage_montage(sel_img, channel_axis = 3 if len(sel_img.shape) == 4 else None)
    else:
        montage_arr = skimage_montage(sel_img, multichannel = (n_channels == 3))
    montage_img = Image.fromarray(montage_arr)

    return montage_img