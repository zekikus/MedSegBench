# MedSegBench: A Comprehensive Benchmark for Medical Image Segmentation in Diverse Data Modalities
Musa Aydin, Zeki Kuş

MedSegBench is a comprehensive benchmark designed to evaluate deep learning models for medical image segmentation across a wide range of modalities. It covers a wide range of modalities, including 35 datasets with over 60,000 images from ultrasound, MRI, and X-ray. The benchmark addresses challenges in medical imaging by providing standardized datasets with train/validation/test splits, considering variability in image quality and dataset imbalances. The benchmark supports binary and multi-class segmentation tasks with up to 19 classes. It supports binary and multi-class segmentation tasks with up to 19 classes and uses the U-Net architecture with various encoder/decoder networks such as ResNets, EfficientNet, and DenseNet for evaluations. MedSegBench is a valuable resource for developing robust and flexible segmentation algorithms and allows for fair comparisons across different models, promoting the development of universal models for medical tasks. It is the most comprehensive study among medical segmentation datasets. The datasets and source code are publicly available, encouraging further research and development in medical image analysis.

# Installation and Requirements
Setup the required environments and install `medsegbench` as a standard Python package from [PyPI]([https://pypi.org/project/medmnist/](https://pypi.org/project/medsegbench/)):

    pip install medsegbench

Or install from source:

    pip install --upgrade git+https://github.com/zekikus/MedSegBench.git

The code requires only common Python environments for machine learning. Basically, it was tested with
* Python 3 (>=3.6)
* PyTorch\==1.3.1
* numpy\==1.18.5, scikit-learn\==0.22.2, Pillow\==8.0.1
* torchvision\==0.11.2
* segmentation-models-pytorch\==0.3.3

# Getting Started

# Experiments

