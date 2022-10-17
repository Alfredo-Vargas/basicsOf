# **dnf** - The package manager of Fedora, CentOS, RedHat ...

- To install or reinstall:

```bash
sudo dnf install htop
sudo dnf reinstall htop
```

- To search using `dnf`

```bash
dnf search apache
```

- List packages installed using `dnf`

```bash
dnf list installed
```

- List recent installations

```bash
dnf list recent
```

- To remove packages

```bash
sudo dnf remove alacritty
```

- Update a particular package

```bash
sudo dnf upgrade <firefox>
```

- Upgrade your system

```bash
sudo dnf upgrade <package>
```

- To remove losing dependencies

```bash
sudo dnf autoremove
```
