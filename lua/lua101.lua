-- BASICS OF COMMENTING
-- Line Comment

--[[
  Block Comment
]]

print("Hello World")

--[[
  nil
  number 1 1.24 0.1 44
  string 'hello' "hello world"
  boolean true false
  table
]]

-- HOW TO DECLARE VARIABLES
local myfirst_VARIABLE = 42
print(myfirst_VARIABLE)

-- HOW TO CONCATENATE STRINGS
local name = "jack"
local surname = "the killer"
local full_name = name .. " " .. surname
print(full_name)

--    MULTILINE STRING
local description = [[Color
 Persistence 
Tag
]]

print(description)

print("Variables Boolean values:")
local var1 = false
local var2 = 0
local var3 = -1
local var4 = ""
local var5 = nil

if not var1 then
 print("not false is considered as true")
end

if var2 then
 print(var2 .. " is considered as true")
end

if var3 then
 print(var3 .. " is considered as true")
end

if var4 then
 print("empty string is considered as true")
end

if var5 then
 print(var5 .. " is considered as true")
end

print("\nGlobal variables")
c = 20  -- this is global variable
_G.Hello = "Hello there!"  --   this is a global variable

print("\nConvert String to number")
local str = "22"
print(type(str))
print(type(tonumber(str)))

print("\nGet random number from 10 to 50")
math.randomseed(os.time())
print(math.random(10, 50))

print("\nThree ways to get the length of string: Hello World")
local str2 = "Hello World"
print(#str2)  -- gives the length of the string

local str3 = #"Hello World"
print(str3)  -- gives the length of the string

print(string.len(str))  -- gives the length of the string

print("\nConvert number to string")
local x = 22
local y = tostring(x)
print(type(x), type(y))

print("\nconvert the string: Hello to lowercase and uppercase:")
local string_test = "Hello"
print(string.lower(string_test))
print(string.upper(string_test))

print("\nSpecial characters include the newline \\n")
print("Special characters include the tab \\t")
print("and the vertical tab: \\v")
print("Hello\nWorld\t!!!!!\v I am Steve")

print("\nSubstring:")
print(string.sub(str2, 0, 5))

print("\nTo get the ascii char representation given its decimal representation")
print(string.char(65))

print("\nTo get the decimal value of a char given its ascii representation")
print(string.byte("A"))

print("\nTo get the decimal value of a string given its ascii representation")
print(string.byte("Hello World", 1, 99))

print("\nTo repeat a string given a separator")
print(string.rep("Hello!", 10, " "))

print("\nTo format a string")
print(string.format("pi: %.2f\nMy age: %i", math.pi, 40))

print("\nTo find something in a string")
print(string.find("Hello World", "orl"))
print(string.match("Hello World", "osrl"))

print("\nTo string substitute")
print(string.gsub("Hello World", "o", "!"))

-- CODE CONTROL FLOW

-- If Statements
if nil then
  print("\nStatement was true")
else
  print("\nThe statement was nil")
end

if (3 ~= 2) and (4 == 2*2) then
  print("\nThree is different than two")
  print("The not equal symbol is ~=")
end

print("\nTernary operator in Lua")
local x9 = -2
local sign = x9 < 0 and 'negative' or 'non-negative'
print("The variable x is " .. sign)

-- LOOPS
print("\nLooping like Python but last index is also taken into account")
for i = 1, 10, 1 do  -- prints the last number unlike python/C
  print(i)
end

print("\nLooping where condition is defined in local variable")
local start_val, end_val, step_val = 10, 1, -1
for i = start_val, end_val, step_val do -- prints the last number unlike python/C
  print(i)
end

print("\nLooping through array values")
local arr = {1, 2, 3, 5, 8, 13}
for i = 1, #arr do
  print(arr[i])
end

print("\nWhile loop")
local peeps = 10
while peeps > 0 do
  peeps = peeps - 1
  print("People left at party: " .. peeps)
end

print("\nRepeat loop")
repeat
  print("hey there!")
  x = x + 1
until x > 10

print("\nUsing user input")
print("What is 10 + 5?")
local ans = io.read()
print("Your answer was: " .. ans)

print("\nUsing io.write() to get the user input")
io.write("Your name is: ")
local name_given = io.read()
print("You gave the name: " .. name_given)

