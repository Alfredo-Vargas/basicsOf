-- ---------- COROUTINES ----------
-- Coroutines are like threads except that they can't run in parallel
-- A coroutine has the status of running, susepnded, dead or normal

-- Use create to create one that performs some action
Co = coroutine.create(function()
  for i = 1, 10, 1 do
  print(i)
  print(coroutine.status(Co))
  if i == 5 then coroutine.yield() end
  end end)

-- They start off with the status suspended
print(coroutine.status(Co))

-- Call for it to run with resume during which the status changes to running
coroutine.resume(Co)

-- After execution it has the status of dead
print(coroutine.status(Co))

local co2 = coroutine.create(function()
  for i = 101, 110, 1 do
  print(i)
  end end)

coroutine.resume(co2)
coroutine.resume(Co)
