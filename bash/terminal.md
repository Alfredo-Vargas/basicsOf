# Terminal Signals and Settings

## Some Linux terminal useful options:

- `setfont ter-132n` : makes your font bigger for your current terminal session

## SIGNALS TO TERMINAL

- `C-c` : sends a stop signal
- `C-z` : sends to background, resume with fg
- `C-s` : suspends terminal
- `C-q` : resumes suspended terminal
- `C-d` : sends end of file signal
- Example

```bash
while true; do echo hello; sleep 1' dome
C-s
C-q
```

