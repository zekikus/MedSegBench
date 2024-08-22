from setuptools import setup, find_packages

import medsegbench


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


README = readme()


setup(
    name='medsegbench',
    version='1.0.0',
    url=medsegbench.HOMEPAGE,
    license='Apache-2.0 License',
    author='Musa Aydin and Zeki Kuş',
    author_email='maydin@fsm.edu.tr;zkus@fsm.edu.tr',
    python_requires=">=3.6.0",
    description='MedSegBench: A Comprehensive Benchmark for Medical Image Segmentation in Diverse Data Modalities',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "scikit-image",
        "Pillow",
        "torch",
        "torchvision",
        "segmentation-models-pytorch"
    ],
    zip_safe=True,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"
    ]
)