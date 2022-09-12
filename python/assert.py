# Use asserts when you are in Defensive Programmer Mode!
x = 2

# Always specify a error message with assert so it becomes more informative
assert x == 1, f"expected 1 but got {x=}"

# Execution of python files with optimization flag will remove:
# Assertions, Doc strings
# Example: python -O assert.py
