# Fix Discord issue Wayland Nvidia Electron issue:

- Simply run the binary `Discord` with one of the two flags:

```bash
Discord --disable-gpu
DIscord --use-gl=desktop
```

- Permanent fix [link here](https://www.reddit.com/r/Fedora/comments/qmv8qi/comment/iqllemg/):

1. `sudo find / -iname "*discord*.desktop"` to find where the global shortcut file is.
2. Copy that global shortcut to ~/.local/share/applications/ and DO NOT RENAME IT. Its filename must STAY EXACTLY THE SAME, which is a requirement if you want it to override the global shortcut.
3. Edit your local version, find all Exec= lines and append the `--use-gl=desktop` parameter to them.
4. Run update-desktop-database ~/.local/share/applications (run as your own user, not with sudo). This writes your account's mime-associations to point at your local Discord desktop file, to handle things like auto-launching discord from web links.
5. Wait or restart your machine. Either way, your custom shortcut should be read by your system after a while (it can take a few minutes on GNOME), and it will then be used whenever you launch Discord via your app menu. If your custom parameter isn't being used, you should restart the machine.


# VSCode Fix

- This fix applies to all electron apps that must run in Wayland

```bash
code --enable-ozone --ozone-platform=wayland
```

# Keepass
