# Cloud Free Image Downloader

A small tool to download cloud free images from GEE. Also serves as an example that projects in the
DLR MF-DAS organization should follow. You should copy the CI/CD set-up and other practices for your repository.

## Installation

This tool relies on Google Earth Engine's Python API which cannot be installed automatically as a
dependency. You need to install it from conda-forge in your conda environment:

```
conda install -c conda-forge earthengine-api
```

This is assuming you already have a conda environment activated.

## Usage