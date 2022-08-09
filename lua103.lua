-- The OS Module
print("How many seconds has passed since 1970?")
print(os.time())
print("How many seconds has passed since 1970 until 2000-10-1 13:20:10?")
print(os.time({
  year = 2000,
  month = 10,
  day = 1,
  hour = 13,
  min = 20,
  sec = 10
}))

print("\nMethod to print the diff time (recent - past):")
print("Use: os.difftime(bigger, smaller)")

print("\nGet the current date")
print(os.date())

print("\nSome environment variables:")
print(os.getenv("HOME"))
print(os.getenv("USER"))

print("\nRename and remove files:")
print("For rename use: os.rename(\"oldName.txt\", \"newName.txt\")")
print("For remove use: os.remove(\"fileName.txt\")")

print("\nExecuting bash commands")
os.execute("whoami")

print("\nCalculate time intervals in your code:")
local start = os.clock()
print(os.clock() - start)

print("\nTo exit the running file")
for i = 1, 10 do
  print(i)
  if i == 5 then
    os.exit()
  end
end
