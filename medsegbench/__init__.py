from medsegbench.info import HOMEPAGE, INFO

#====================================================================
# This part of the code is based on MedMNIST
# from https://github.com/MedMNIST/MedMNIST
# Yang, J., Shi, R., Wei, D., Liu, Z., Zhao, L., Ke, B., ... & Ni, B. (2023). Medmnist v2-a large-scale lightweight benchmark for 2d and 3d biomedical image classification. Scientific Data, 10(1), 41.
# ===================================================================

try:
    from medsegbench.dataset import (KvasirMSBench, Isic2018MSBench, DriveMSBench, ChaseDB1MSBench, Dca1MSBench,
                                  ChuacMSBench, WbcMSBench, IdribMSBench, CellnucleiMSBench, PandentalMSBench,
                                  Bbbc010MSBench, DynamicNuclearMSBench, NusetMSBench, NucleiMSBench, TnbcnucleiMSBench,
                                  MonusacMSBench, DeepbacsMSBench, BriFiSegMSBench, BusiMSBench, Covid19RadioMSBench,
                                  CovidQUExMSBench, CystoFluidMSBench, Isic2016MSBench, PolypGenMSBench, Promise12MSBench,
                                  RoboToolMSBench, UWSkinCancerMSBench, UltrasoundNerveMSBench, USforKidneyMSBench,
                                  YeazMSBench, BkaiIghMSBench, M2caiSegMSBench, AbdomenUSMSBench, FHPsAOPMSBench, MosMedPlusMSBench)
except:
    print("Please install the required packages first. " +
          "Use `pip install -r requirements.txt`.")