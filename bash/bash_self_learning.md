# Bash Scripting

## Some Concepts

- `POSIX` : **P**ortable **O**perating **S**ystem **I**nterface UNI**X**, an attempt to standardize UNIX-like OSes.
- `sh scriptname, bash scriptname` : used to invoke scripts, avoid `sh <scriptname` (this disables reading from `stdin`)
- For security reasons the current directory `(./)` is not by default included in a user's `$PATH`
- Variables better than hard-coded values
- Positional arguments:
  - `$0` is the name of the script itself
  - `$1` is the first argument
  - `$2` is the second argument
  - ...
  - `${10}` is the tenth argument
  - `${11}` is the eleventh argument

## Bash snippets

- To control if the script parameters are correct:

```Bash
E_WRONG_ARGS=85
script_parameters="-a -h -m -z"
#                  -a = all, -h = help, etc.

if [ $# -ne $Number_of_expected_args ]
then
  echo "Usage: `basename $0` $script_parameters"
  # `basename $0` is the script's filename.
  exit $E_WRONG_ARGS
fi
```

- Self deleting script

```bash
#!/bin/rm
# Self-deleting script.

# Nothing much seems to happen when you run this... except that the file disappears.

WHATEVER=85

echo "This line will never print (betcha!)."

exit $WHATEVER  # Doesn't matter. The script will not exit here.
                # Try an echo $? after script termination.
                # You'll get a 0, not a 85.
```

- Change to uppercase in bash

```bash
name="john"
echo ${name^^}
```

- Loop over chars in a string
```bash
greet="hello world"
for (( i=0; i<${#greet}; i++ )); do
  echo "${greet:$i:1}"
done
```
