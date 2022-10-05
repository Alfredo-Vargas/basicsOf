# Miniconda Cheat Sheet

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
