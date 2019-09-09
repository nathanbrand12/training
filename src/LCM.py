def lcm(x, y):
  if x > y:
        greater = x
  else:
        greater = y
  while(True):
     if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
     greater += 1
  return lcm

num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
result = lcm(num1, num2)
print(result)
