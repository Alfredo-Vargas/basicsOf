-- A Table is a container for multiple variables
local arr = {10, true, "hello world", 2.4}
print("The elements of the array are:")
for i = 1, #arr do  -- index start from 1, out of scope variables will return nil
  print(arr[i])
end
print("Length of the array is: " .. #arr)
print("The last element of the array is: " .. arr[#arr])

local arr2 = {4, 3, 2, 1, 0}
table.sort(arr2)
for i = 1, #arr2 do
  print(arr2[i])
end

-- Other table methods include:
print("table.insert(array, index, \"new_content\")")
print("table.remove(array, index)")

-- Array items concatenation
local array_greeting = {"hello", "world", "I", "am", "steve"}
print(table.concat(array_greeting, " "))

-- Mutidimensional Table is a Table inside another table
local parent_table = {
  {1, 2, 3, 8, 0},
  {6, 8, 0},
  {9, 99, 989}
}
print(parent_table[2][1])
for i = 1, #parent_table do
  for j = 1, #parent_table[i] do
    print(parent_table[i][j])
  end
end

print("\nFunction block:")
local function displayAge(age)
  age = age or 5  -- default value
  print("You are " .. age .. " years old")
  print("You will be " .. age +2 .. " years old in 2 years")
  print("You were " .. age - 1 .. " year old last year")
end

displayAge()
print()
displayAge(20)

local add10 = function (number)
  local outcome = 10 + number
  return number, outcome
end

local _, output = add10(20)
print("Had 10 added to it: " .. output)

print("\nArguments passed as table for function input")
local function sum(...)
  local sums = 0
  for key, value in pairs({...}) do
    print(key, value)
    sums = sums + value
  end

  return "sum of values gives: " .. sums
end

print(sum(10, 5, 9, 0, 14))

-- COROUTINE is an async await function
local routine_1 = coroutine.create(
  function ()
    for i = 1, 10, 1 do
      print("(Routine 1): " .. i)
      if i == 5 then
        coroutine.yield()  -- to wait before continuing
      end
    end
  end
)

local routine_func = function ()
  for i = 11, 20 do
    print("(Routine 2): " .. i)
  end
end

local routine_2 = coroutine.create(routine_func)

coroutine.resume(routine_1)
coroutine.resume(routine_2)
coroutine.resume(routine_1) -- dead next if block wont' be executed

if coroutine.status(routine_1) == "suspended" then
  coroutine.resume(routine_1)
end
