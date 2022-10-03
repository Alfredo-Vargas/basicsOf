# Miniconda Cheat Sheet

## Create conda virtual environments

### Basic Tool environments

```console
conda create -n my-tools -c conda-forge python numpy matplotlib jupyterlab theme-darcula jupyterlab_vim jupyterlab-lsp
```

- Extra theme, not in anaconda official repository: [onedarkpro](https://github.com/johnnybarrels/jupyterlab_onedarkpro)

### Fastai

```console
conda create -n pt-intro -c conda-forge numpy
conda activate pf-intro
conda install -c pytorch pytorch cudatoolkit
<!-- conda install -c pytorch pytorch cudatoolkit -->
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

### Export and create/update an environment from a txt or yml file

```console
conda list --explicit > envname-modules.txt
conda env export --name envname > envname.yml
conda env create --file envname.yml
conda env update --file my-tools.yml
conda env update --name envname --file my-tools.yml
```

- To clone an environment
  `conda create --clone envname --name new-envname`

- To update environment and dependencies
  `conda env update --prefix ./env --file environment.yml --prune`

- If a file named environment.yml is present in a directory you could create an environment by
  `conda env create`

### Environment Commands

- To list environments installed:
  `conda env list`
  `conda env --name envname`

- To activate/deactivate environments:
  `conda activate envname`
  `conda deactivate`

### Add/Remove Conda Packages

`conda install package-name`
`conda install package-name=X.Y`
`conda remove --name envname pkg1 pkg2 ...`


### To show or add conda channels

```console
conda config --show channels
conda config --add channels channelname
```

### Base conda

- To NOT activate conda by default
  `conda config --set auto_activate_base false`

- Verify conda installation and update base conda
  `conda info`
  `conda update -n base conda`
