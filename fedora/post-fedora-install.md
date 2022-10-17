# Guidelines to set up fedora on My Desktop

```bash
sudo dnf update
sudo dnf upgrade --refresh -y
sudo dnf install gnome-shell-extension-appindicator
sudo dnf install gnome-extensions-app
sudo dnf install vim neovim alacritty jetbrains-mono-fonts tilix df-find
```

## add ssh keys to your account to link to github

[github ssh config](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## Install Nvidia Drivers (worked together with Wayland!)

```bash
lshw -C display
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

```bash
sudo dnf install akmod-nvidia -y

sudo dnf install xorg-x11-drv-nvidia-cuda
reboot
```

## Enable Fractional Scaling in Wayland

- Enable this in the terminal:

```bash
gsettings set org.gnome.mutter experimental-features “[‘scale-monitor-framebuffer’]”
```
