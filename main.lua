print("\nImporting Custom Modules")
print("A module is a lua file that returns a single table when called")
local mod = require("myCustomModule")

print(mod.add(5, 10))

print("\nSimulating OOP by Using Lua Tables as return values of functions")
print("Lua as C have tables / Structures that contain other data types\n")
local t = {
  name = "Jack",
  age = 18,
  friends = {"Fred"},
}
print(t.name)

local function Pet(name)
    name = name or "Luis"
  return {
    name = name,
    status = "Hungry",
    feed = function(self)
      print(name .. " is fed")
      self.status = "Full"
    end
  }
end

local cat = Pet("Kitty")
local dog = Pet()
print(cat.status)
cat:feed()
print(cat.status)
print(dog.status)


print("\nInheritance Examples")

local function Dog(name, breed)
  local dog = Pet(name)
  dog.breed = breed
  dog.loyalty =0
  dog.isLoyal = function(self)
    return self.loyalty >= 10
  end
  dog.feed = function(self)
    print(name .. " is fed")
    self.status = "full"
    self.loyalty = self.loyalty + 5
  end
  dog.bark = function(self)
    print("Woof Woof")
  end
  return dog
end

local lassy = Dog("Lassy", "Poodle")
lassy:feed()
lassy:feed()
print(lassy.status)
print(lassy.breed)
lassy:bark()

if lassy:isLoyal() then
  print("Will protect against intruder")
else
  print("Will NOT protect against intruder")
end

print("\nMetamethods")
print("\nSimilar to operator overloading")

local function addTableValues(x, y)
  return x.num + y.num
end

local metatable = {
  __add = addTableValues,  -- __add means PLUS: +
  __sub = function (x, y)
    return x.num - y.num
  end
}

--[[
  __add = +
  __sub = -
  __mul = *
  __div = /
  __mod = %
  __pow = ^
  __concat = ..
  __len = #
  __eq = ==
  __lt = <
  __le = <=
  __gt = >
  __ge = >=
]]


local tbl1 = { num = 50 }
local tbl2 = { num = 10 }

setmetatable(tbl1, metatable)

local sumtable = tbl1 + tbl2
local subtable = tbl1 - tbl2

print(sumtable)
print(subtable)
