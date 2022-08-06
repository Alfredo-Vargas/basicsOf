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

local myfirst_VARIABLE = 42
print(myfirst_VARIABLE)

local name = "jack"
local surname = "the killer"
local full_name = name .. " " .. surname
print(full_name)

-- Multiline string
local description = [[Color
 Persistence 
Tag
]]

print(description)

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

c = 20  -- this is global variable
_G.Hello = "Hello there!"  --   this is a global variable

local str = "22"
print(type(str))
print(type(tonumber(str)))

-- random number
print("Random Number Example:")
math.randomseed(os.time())
print(math.random(10, 50))

local str2 = "Hello World"
print(#str2)  -- gives the length of the string

local str3 = #"Hello World"
print(str3)  -- gives the length of the string

local x = 22
local y = tostring(x)
print(type(x), type(y))
