# This Command List applies also to the base distro Ubuntu - Debian

- How to install and remove using apt

```bash
sudo apt install <package-name>
sudo apt remove <package-name>
```

- To completely remove dependencies

```bash
sudo apt --purge remove <package-name>
sudo apt purge <package-name>
```

- To clean your the dependencies system-wide:

```bash
sudo apt autoremove
sudo apt --purge autoremove
```

- Change the `python3` as the default `python`

```bash
sudo apt install python-is-python3
```
