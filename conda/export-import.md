# Export and create/update conda environments

## Export conda environment as txt

```console
conda list --explicit > envname-modules.txt
```

## Export conda environment as yml

```console
conda env export --name envname > envname.yml
```

## Create conda environment from file

```console
conda env create --file envname.yml
```

## Update conda environment from a file

```console
conda env update --file my-tools.yml
conda env update --name envname --file my-tools.yml
conda env update --prefix ./env --file environment.yml --prune
```

- To clone an environment
  `conda create --clone envname --name new-envname`
