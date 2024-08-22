from medsegbench.info import HOMEPAGE, INFO

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