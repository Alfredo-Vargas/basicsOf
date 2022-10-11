# Environment Templates

## For LunarVim PythonIDE

```console
conda install -c conda-forge python pyright black flake8
```

## Basic Plugins for your environments

<!-- TODO: Remove python  -->

```console
conda create -n my-plugins -c conda-forge jupyterlab theme-darcula jupyterlab_vim jupyterlab-lsp
```

- Extra theme, not in anaconda official repository: [onedarkpro](https://github.com/johnnybarrels/jupyterlab_onedarkpro)

## Fastai

```console
conda create -n pt-intro -c conda-forge numpy
conda activate pt-intro
conda install -c pytorch pytorch cudatoolkit
pip install duckduckgo_search
conda install -c fastai fastcore fastdownload
conda install -c fastchan fastai
```

### OpenCV

- NOTE: `opencv-python-headless` does not include GUI support
- NOTE: `conda` does not contain `opencv-contrib-python`, use pip install instead

### Old packages using jupyter notebook

```console
conda install jupyternotebook
conda install -c conda-forge jupyterthemes
```

### AWS-SDK-Python

```console
conda -c create aws-python -c conda-forge python boto3
```
