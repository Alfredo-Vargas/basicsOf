# Clipboard commands

## Xorg

- To copy the contents of a file into the system clipboard (xorg)

```bash
xclip -sel clip <input_file>
```

## Wayland

- To copy the contents of a file into the system clipboard (wayland)

```bash
wl-copy < <input_file>
```

- To paste the contents of the clipboard to a file

```bash
wl-paste > <input_file>
```

- Copy previous command

```bash
wl-copy !!
```
