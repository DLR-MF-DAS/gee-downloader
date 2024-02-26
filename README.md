# Cloud Free Image Downloader

A small tool to download cloud free images from GEE. Also serves as an example that projects in the
DLR MF-DAS organization should follow. You should copy the CI/CD set-up and other practices for your repository.

## Installation

This tool relies on Google Earth Engine's Python API which cannot be installed automatically as a
dependency. You need to install it from conda-forge in your conda environment:

```
conda install -c conda-forge earthengine-api
```

This is assuming you already have a conda environment activated. To install from source code you can
do the following:

```
git clone git@github.com:DLR-MF-DAS/gee_downloader.git
cd gee_downloader
pip install -e .
```
Or if you don't want the source code you can do:

```
pip install git+git@github.com:DLR-MF-DAS/gee_downloader.git
```

## Usage
