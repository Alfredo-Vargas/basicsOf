import sys

# ----- DATA TYPES -----
# Data in Python is dynamically typed and that
# data type can change
# All data is an object which I cover later
# The basic types are integers, floats,
# complex numbers, strings, booleans
# Python doesn't have a character type

# How to get the type
print(type(10))

# There is no limit to the size of integers
# This is a way to get a practical max size
print(sys.maxsize)

# Floats are values with decimal values
# This is how to get a max float
print(sys.float_info.max)

# But, they are accurate to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# Complex numbers are [real part]+[imaginary part]
cn1 = 5 + 6j

# Booleans are either True or False
b1 = True

# Strings are surrounded by ' or "
str1 = "Escape Sequences ' \t \" \\ and \n"

str2 = '''Triple quoted strings can contain ' and "'''

# You can cast to different types with int, float,
# str, chr
print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord("a")))  # to int

# ----- OUTPUT -----
# You can define a separator for print
print(12, 21, 1974, sep="/")

# Eliminate newline
print("No Newline", end="")

# String formatting %e for exponent
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, "A"))
