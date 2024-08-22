import os
from os.path import expanduser
import warnings

def get_default_root():
    home = expanduser("~")
    dir_path = os.path.join(home, ".medsegbench")

    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except:
        warnings.warn("Failed to setup default root.")
        dir_path = None
    
    return dir_path

# CONSTANTS
DEFAULT_ROOT = get_default_root()
HOMEPAGE = "https://github.com/zekikus/MedSegBench"

INFO = {
    'kvasir': {
        'python_class' : "KvasirMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 700, 'val' : 100, 'test' : 200},
        'license' : 'The use of the Kvasir-SEG dataset is restricted for research and educational purposes. The use of the Kvasir-SEG dataset for commercial purposes is forbidden without prior written permission.',
        'reference': '10.1007/978-3-030-37734-2_37, https://datasets.simula.no/kvasir-seg/'
    },
    
    'isic2018': {
        'python_class' : "Isic2018MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 2594, 'val' : 100, 'test' : 1000},
        'license' : 'CC BY-NC 4.0',
        'reference': '10.48550/arXiv.1902.03368, 10.1038/sdata.2018.161, https://challenge.isic-archive.com/data/#2018'
    },    
    'drive': {
        'python_class' : "DriveMSBench",
        'description' : "",
        'url_128' : 'https://zenodo.org/records/12732404/files/drive_128.npz?download=1',
        'MD5_128' : '7300fb561dcd7c8d3638724d182acfe1',
        'url_256' : 'https://zenodo.org/records/12732404/files/drive_256.npz?download=1',
        'MD5_256' : '26c7cf19f86d7ab0f1d70346b2fce7b5',
        'url_512' : 'https://zenodo.org/records/12732404/files/drive_512.npz?download=1',
        'MD5_512' : 'b6589f9213337b9429243d68a07bbf69',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 18, 'val' : 2, 'test' : 20},
        'license' : 'CC-BY-4.0',
        'reference': '10.1109/TMI.2004.825627, https://drive.grand-challenge.org/'
    },

    'chasedb1': {
        'python_class' : "ChaseDB1MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 19, 'val' : 2, 'test' : 7},
        'license' : 'CC BY 4.0',
        'reference': '10.1016/j.bspc.2018.06.007, https://blogs.kingston.ac.uk/retinal/chasedb1/'
    },

    'dca1': {
        'python_class' : "Dca1MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 93, 'val' : 13, 'test' : 28},
        'license' : 'This database represents the first set of angiograms and ground-truth images made accessible to the scientific community for research and comparison purposes',
        'reference': 'https://doi.org/10.3390/app9245507, http://personal.cimat.mx:8181/~ivan.cruz/DB_Angiograms.html'
    },

    'chuac': {
        'python_class' : "ChuacMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 21, 'val' : 3, 'test' : 6},
        'license' : 'CC BY 4.0',
        'reference': 'https://figshare.com/s/4d24cf3d14bc901a94bf'
    },

    'wbc': {
        'python_class' : "WbcMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'cytoplasm',
            '2' : 'nucleus'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 280, 'val' : 40, 'test' : 80,
                       'train_C1' : 146, 'val_C1' : 20, 'test_C1' : 43,
                       'train_C2' : 63, 'val_C2' : 9, 'test_C2' : 18,
                       'train_C3' : 44, 'val_C3' : 6, 'test_C3' : 13,
                       'train_C4' : 23, 'val_C4' : 3, 'test_C4' : 8,},
        'license' : 'CC BY 4.0',
        'class_names' : {"C1" : "Lymphocyte", "C2" : "Monocyte", "C3": "Neutrophil", "C4": "Eosinophil"},
        'reference': '10.1016/j.micron.2018.01.010, 10.1016/j.cmpb.2019.105020'
    },

    'idrib': {
        'python_class' : "IdribMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 47, 'val' : 6, 'test' : 27,
                       'train_C1': 47, 'val_C1': 6, 'test_C1': 27,
                       'train_C2': 47, 'val_C2': 6, 'test_C2': 27,
                       'train_C3': 47, 'val_C3': 6, 'test_C3': 27,
                       'train_C4': 47, 'val_C4': 6, 'test_C4': 27},
        'license' : 'CC BY 4.0',
        'class_names' : {"C1" : "Microaneurysms", "C2" : "Hemorrhages", "C3": "Hard Exudates", "C4": "Optic Disc"},
        'reference': '10.3390/data3030025, 10.21227/H25W98'
    },

    'cellnuclei': {
        'python_class' : "CellnucleiMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 469, 'val' : 67, 'test' : 134},
        'license' : 'CC0',
        'reference': '10.1038/s41592-019-0612-7, https://www.kaggle.com/competitions/data-science-bowl-2018/data'
    },

    'pandental': {
        'python_class' : "PandentalMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            'non-zero' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 81, 'val' : 11, 'test' : 24},
        'license' : 'CC BY 4.0',
        'reference' : '10.1117/1.JMI.2.4.044003, 10.17632/hxt48yk462.1'
    },

    'bbbc010': {
        'python_class' : "Bbbc010MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 70, 'val' : 10, 'test' : 20},
        'license' : 'Does not have copyright information',
        'reference': 'https://bbbc.broadinstitute.org/BBBC010, 10.1038/nmeth.2083'
    },

    'dynamicnuclear': {
        'python_class' : "DynamicNuclearMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            'non-zero' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 4950, 'val' : 1417, 'test' : 717},
        'license' : 'Modified Apache 2.0',
        'reference': '10.1371/journal.pcbi.1005177, https://datasets.deepcell.org/data'
    },

    'nuset': {
        'python_class' : "NusetMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 2385, 'val' : 340, 'test' : 683},
        'license' : 'CC BY 4.0',
        'reference': '10.1371/journal.pcbi.1008193, 10.5281/zenodo.3996369,'
    },

    'nuclei': {
        'python_class' : "NucleiMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 98, 'val' : 14, 'test' : 29},
        'license' : 'BSD-3',
        'reference': '10.4103/2153-3539.186902, https://andrewjanowczyk.com/use-case-1-nuclei-segmentation/'
    },

    'tnbcnuclei': {
        'python_class' : "TnbcnucleiMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 35, 'val' : 5, 'test' : 10},
        'license' : 'CC BY 4.0',
        'reference': '10.1109/TMI.2018.2865709, https://zenodo.org/records/2579118'
    },

    'monusac': {
        'python_class' : "MonusacMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'Epithelial',
            '2' : 'Lymphocyte',
            '3' : 'Macrophage',
            '4' : 'Neutrophil',
            '5' : 'Ambiguous'          
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 188, 'val' : 21, 'test' : 101},
        'license' : 'CC BY-NC-SA 4.0',
        'reference': '10.1109/TMI.2021.3085712, https://monusac-2020.grand-challenge.org/Data/'
    },

    'deepbacs': {
        'python_class' : "DeepbacsMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 17, 'val' : 2, 'test' : 15 },
        'license' : 'CC BY 4.0',
        'reference': '10.1038/s42003-022-03634-z, 10.5281/zenodo.5550934'
    },

    'brifiseg': {
        'python_class' : "BriFiSegMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 1005, 'val' : 115, 'test' : 240,
                       'train_C1' : 201, 'val_C1' : 23, 'test_C1' : 48,
                       'train_C2' : 201, 'val_C2' : 23, 'test_C2' : 48,
                       'train_C3' : 201, 'val_C3' : 23, 'test_C3' : 48,
                       'train_C4' : 201, 'val_C4' : 23, 'test_C4' : 48,
                       'train_C5' : 201, 'val_C5' : 23, 'test_C5' : 48},
        'class_name': {"C1": "Target 1 A549", "C2":"Target 2 A549", "C3": "HeLa", "C4": "MCF7", "C5": "RPE1"},
        'license' : 'CC BY 4.0',
        'reference': 'https://arxiv.org/pdf/2211.03072, https://zenodo.org/records/7195636'
    },

    # X
    'busi': {
        'python_class' : "BusiMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 452, 'val' : 64, 'test' : 131,
                       'train_C1' : 305, 'val_C1' : 43, 'test_C1' : 89,
                       'train_C2' : 147, 'val_C2' : 21, 'test_C2' : 42},
        'class_names' : {"C1" : "benign", "C2" : "malignant"},
        'license' : 'CC0: Public Domain',
        'reference': '10.1016/j.dib.2019.104863, https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset'
    },

    'covid19radio': {
        'python_class' : "Covid19RadioMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 14814, 'val' : 2115, 'test' : 4236,
                       'train_C1' : 2531,  'val_C1' : 361,  'test_C1' : 724,
                       'train_C2' : 4208,  'val_C2' : 601,  'test_C2' : 1203,
                       'train_C3' : 7134,  'val_C3' : 1019, 'test_C3' : 2039,
                       'train_C4' : 941,   'val_C4' : 134,  'test_C4' : 270},
        'class_names' : {"C1" : "covid", "C2" : "lung", "C3": "normal", "C4": "viral pneumonia"},
        'license' : 'Academic/Non-Commercial Use',
        'reference': '10.1109/ACCESS.2020.3010287, 10.1016/j.compbiomed.2021.104319, https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database'
    },

    'covidquex': {
        'python_class' : "CovidQUExMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 1864, 'val' : 466, 'test' : 583 },
        'license' : 'CC BY-SA 4.0',
        'reference': '10.1016/j.compbiomed.2021.105002, 10.34740/kaggle/dsv/3122958, 10.1016/j.compbiomed.2021.104319, 10.1007/s13755-021-00146-8, 10.1109/ACCESS.2020.3010287, https://www.kaggle.com/datasets/anasmohammedtahir/covidqu' 
    },
    
    'cystoidfluid': {
        'python_class' : "CystoFluidMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 703, 'val' : 101, 'test' : 202 },
        'license' : 'CC BY-NC-SA 4.0',
        'reference': '10.1109/TMI.2021.3057884, 10.34740/KAGGLE/DS/2277068, https://doi.org/10.1002/ima.22662'
    },

    'isic2016': {
        'python_class' : "Isic2016MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 810, 'val' : 90, 'test' : 379},
        'license' : 'CC BY-NC 4.0',
        'reference': '10.1109/ISBI.2018.8363547, https://challenge.isic-archive.com/data/#2016'
    }, 

    'polypgen': {
        'python_class' : "PolypGenMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 984, 'val' : 140, 'test' : 288,
                       'train_C1' : 176, 'val_C1' : 24, 'test_C1' : 51,
                       'train_C2' : 190, 'val_C2' : 28, 'test_C2' : 52,
                       'train_C3' : 318, 'val_C3' : 45, 'test_C3' : 93,
                       'train_C4' : 98,  'val_C4' : 15, 'test_C4' : 33,
                       'train_C5' : 144, 'val_C5' : 20, 'test_C5' : 42,
                       'train_C6' : 58,  'val_C6' : 8,  'test_C6' : 17},
        'license' : 'CC BY 4.0',
        'annotations': {"C1": "Ambroise Paré Hospital, Paris, France",
                        "C2": "Istituto Oncologico Veneto, Padova, Italy",
                        "C3": "Centro Riferimento Oncologico, IRCCS, Italy",
                        "C4": "Oslo University Hospital, Oslo, Norway",
                        "C5": "John Radcliffe Hospital, Oxford, UK",
                        "C6": "University of Alexandria, Alexandria, Egypt"},
        'reference': '10.48550/arXiv.2202.12031, 10.1016/j.media.2021.102002'
    }, 

    'promise12': {
        'python_class' : "Promise12MSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 1031, 'val' : 147, 'test' : 295},
        'license' : 'Does not have copyright information',
        'reference': '10.1016/j.media.2013.12.002, 10.5281/zenodo.8014040'
    }, 

    'robotool': {
        'python_class' : "RoboToolMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 350, 'val' : 50, 'test' : 100},
        'license' : 'CC BY 4.0.',
        'reference' : '10.1109/TMI.2021.3057884, https://www.synapse.org/Synapse:syn22427422, arXiv.1902.06426'
    }, 

    'uwaterlooskincancer': {
        'python_class' : "UWSkinCancerMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 143, 'val' : 19, 'test' : 44,
                       'train_C1' : 83, 'val_C1' : 11, 'test_C1' : 25,
                       'train_C2' : 60, 'val_C2' : 8, 'test_C2' : 19,},
        'license' : 'Non-commercial use',
        'class_names' : {"C1" : "melenoma", "C2" : "notmelenoma"},
        'reference': 'https://uwaterloo.ca/vision-image-processing-lab/research-demos/skin-cancer-detection'
    }, 

    'ultrasoundnerve': {
        'python_class' : "UltrasoundNerveMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 1651, 'val' : 223, 'test' : 449},
        'license' : 'Does not have copyright information',
        'reference': 'https://www.kaggle.com/competitions/ultrasound-nerve-segmentation/overview'
    }, 

    'usforkidney': {
        'python_class' : "USforKidneyMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 3210, 'val' : 458, 'test' : 918},
        'license' : 'GPL 2',
        'reference': '10.1016/j.ultras.2022.106706, https://www.kaggle.com/datasets/siatsyx/ct2usforkidneyseg/data'
    }, 

    'yeaz': {
        'python_class' : "YeazMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'foreground'            
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' : 360, 'val' : 96, 'test' : 251},
        'license' : 'Does not have copyright information',
        'reference': '10.1038/s41467-020-19557-4, https://www.epfl.ch/labs/lpbs/data-and-software/'
    },

    'bkai-igh': {
        'python_class' : "BkaiIghMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'neoplastic polyps',
            '2' : 'non-neoplastic polyps'           
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' :  700, 'val' : 100, 'test' : 200},
        'license' : 'BKAI-IGH NeoPolyp-Small is a public dataset released by BKAI Research Center, Hanoi University of Science and Technology incorporation with Institute of Gastroenterology and Hepatology (IGH), Vietnam.',
        'reference': '10.1007/978-3-030-90436-4_2, 10.1109/ACCESS.2022.3195241, arXiv:2307.06420, 10.1109/ACCESS.2022.3168693'
    },

    'm2caiseg': {
        'python_class' : "M2caiSegMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0' : 'unknown',
            '1' : 'grasper',
            '2' : 'bipolar',
            '3' : 'hook',
            '4' : 'scissors',
            '5' : 'clipper',
            '6' : 'irrigator',
            '7' : 'specimen-bag',
            '8' : 'trocars',
            '9' : 'clip',
            '10': 'liver',
            '11': 'gall-bladder',
            '12': 'fat',
            '13': 'organ',
            '14': 'artery',
            '15': 'intestine',
            '16': 'bile',
            '17': 'blood',
            '18': 'black'         
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' :  245, 'val' : 307, 'test' : 62},
        'license' : 'CC BY-NC 4.0',
        'reference': 'https://doi.org/10.48550/arXiv.2008.10134, https://www.kaggle.com/datasets/salmanmaq/m2caiseg'
    },

    'abdomenus': {
        'python_class' : "AbdomenUSMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0' : 'background',
            '1' : 'liver',
            '2' : 'kidney',
            '3' : 'pancreas',
            '4' : 'vessels',
            '5': 'adrenals',
            '6': 'gallbladder',
            '7': 'bones',
            '8' : 'spleen'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' :  569, 'val' : 64, 'test' : 293},
        'license' : 'This dataset has been publicly released after winning a Kaggle Open Data Research Grant.',
        'reference': '10.1007/s11548-019-02046-5, https://www.kaggle.com/datasets/ignaciorlando/ussimandsegm/data'
    },

    'fhpsaop': {
        'python_class' : "FHPsAOPMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'multi-class',
        'pixel_labels'   : {
            '0': 'background',
            '1': 'pubic symphysis',
            '2': 'fetal head'
        },
        'n_channels_im' : 1,
        'n_channels_lbl': 1,
        'n_samples' : {'train' :  2800, 'val' : 400, 'test' : 800},
        'license' : 'CC BY-NC 4.0',
        'reference': '10.1016/j.dib.2022.107904,  10.5281/zenodo.7851338'
    },

    'mosmedplus': {
        'python_class' : "MosMedPlusMSBench",
        'description' : "",
        'url_128' : '',
        'MD5_128' : '',
        'url_256' : '',
        'MD5_256' : '',
        'url_512' : '',
        'MD5_512' : '',
        'task'    : 'binary',
        'pixel_labels'   : {
            '0': 'background',
            '1': 'foreground'
        },
        'n_channels_im' : 3,
        'n_channels_lbl': 1,
        'n_samples' : {'train' :  1910, 'val' : 272, 'test' : 547},
        'license' : 'CC BY-NC-ND 3.0',
        'reference': '10.48550/arXiv.2005.06465, https://figshare.com/authors/MedSeg/9940190, https://www.kaggle.com/datasets/maedemaftouni/covid19-ct-scan-lesion-segmentation-dataset'
    },

}
