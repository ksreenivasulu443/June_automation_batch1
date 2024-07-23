var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

for num in range(2,-5,-1):
    print(num, end=', ')


a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')

x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

for i in range(1,10):
    print(i)
else:
    print("esle",i)

for num in range(-2,-5,-1):
    print(num, end=", ")

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

x = 0
while (x < 100):
  x+=2
print(x)

for l in 'Jhon':
   if l == 'o':
      break
   print(l, end=", ")

for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break
