-- Prints to the screen (Can end with semicolon)
print("Hello World")

--[[
Multiline comment
]]

-- Variable names can't start with a number, but can contain letters, numbers
-- and underscores

-- Lua is dynamically typed based off of the data stored there
-- This is a string and it can be surrounded by ' or "
name = "Derek"

-- Another way to print to the screen
-- Escape Sequences : \n \b \t \\ \" \'
-- Get the string size by proceeding it with a #
io.write("Size of string ", #name, "\n")

-- You can store any data type in a variable even after initialization
name = 4
io.write("My name is ", name, "\n")

-- Lua only has floating point numbers and this is the max number
bigNum = 9223372036854775807 + 1
io.write("Big Number ", bigNum, "\n")

io.write("Big Number ", type(bigNum), "\n")

-- Floats are precise up to 13 digits
floatPrecision = 1.999999999999 + 0.0000000000005
io.write(floatPrecision, "\n")

-- We can create long strings and maintain white space
longString = [[
I am a very very long
string that goes on for
ever]]
io.write(longString, "\n")

-- Combine Strings with ..
longString = longString .. name
io.write(longString, "\n")

-- Booleans store with true or false
isAbleToDrive = true
io.write(type(isAbleToDrive), "\n")

-- Every variable gets the value of nil by default meaning it has no value
io.write(type(madeUpVar), "\n")
