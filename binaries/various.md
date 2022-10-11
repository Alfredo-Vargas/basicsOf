# Common, Useful and Dangerous Commands

- To print the first n-lines of a file

```bash
head --lines <number> <file>
```

- How to remove a file with name -

```bash
touch ./-
rm ./-
```

## tee

- Read from `stdin` and write to `stdout` and files

```bash
echo "yo" | tee path/to/file
ls /usr/bin | tee ls.txt | grep zip
```

## sed : stream editor

- Has the following structure: `sed "sed_command" "file"`, the output goest to stdout

- `sed` can use as separators: `/`, `|` or `#`

- `sed` search for pattern and replace

```bash
sed /line_pattern/s/find/replace/ <file>
```

- Print the first eleven lines:

```bash
sed 11q <file>
```

- The `g` stands for global applicability and the flag `-i` means to write to the file given.

```bash
sed -i "s/find/replace/g <file>"
```

- After substitution deletes lines that match the pattern

```bash
sed "s/find/replace/g; /pattern/ d" <file>`
```

- The flag `-e` is required whenever multiple substitutions are placed.

```bash
sed -e s/find1/replace1/g -e s/find2/replace2/g
```

```bash
sed -n '/pattern/p
```

- Remove extra spaces at the end of a line from a file:

```bash
sed -i 's/ *$//' <file>
```

- Remove extra tabs at the end of a line from a file:

```bash
sed -i 's/[[:space:]]*$//' <file>
```

- Remove empty lines:

```bash
sed -i '/^$/d' <file>
```

- Change lower case to upper case (change U to L and [a-z] to [A-Z] for the contrary):

```bash
sed -i 's/[a-z]/\U&/g' <file>
```

## cat

- Concatenates files and sends it to `stdout`

```console
cat file1 file2
tac file1 file2
```

## Terminal Bombs

- Dangerous do not ever type in your terminal:

```bash
:(){ :|:& };;
```
