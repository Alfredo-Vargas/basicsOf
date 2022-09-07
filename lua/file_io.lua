-- ---------- FILE I/O ----------
-- Different ways to work with files
-- r: Read only (default)
-- w: Overwrite or create a new file
-- a: Append or create a new file
-- r+: Read & write existing file
-- w+: Overwrite read or create a file
-- a+: Append read or create file

-- Create new file for reading and writing
local file = io.open("test.lua", "w+")

-- Write text to the file
if file ~= nil then
  file:write("Random string of text\n")
  file:write("Some more text\n")
else
  io.write("You cannot open the file")
end

-- Move back to the beginning of the file
if file ~= nil then
  file:seek("set", 0)
else
  io.write("You cannot modify the file handler")
end

-- Read from the file
if file ~= nil then
  print(file:read("*a"))
else
  io.write("You cannot read the file")
end


-- Close the file
if file ~= nil then
  file:seek("set", 0)
else
  io.write("You cannot change the file handler")
end

if file ~= nil then
  file:close()
else
  io.write("You cannot close the file")
end

-- Open file for appending and reading
if file ~= nil then
  file = io.open("test.lua", "a+")
else
  io.write("You cannot open the file to append")
end

if file ~= nil then
  file:write("Even more text\n")
  file:seek("set", 0)
else
  io.write("You cannot write to the file")
end


if file ~= nil then
  print(file:read("*a"))
else
  io.write("You cannot read the file")
end

if file ~= nil then
  file:close()
else
  io.write("You cannot close the file")
end
