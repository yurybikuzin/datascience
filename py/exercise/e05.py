#!/usr/bin/python3

for i in range(1, 10 + 1):
  print(i, i**2, i**3)

print('========================')


number = 84
for i in range(1, number + 1):
  if number % i == 0:
    print(i)

print('========================')

num_1 = 12
num_2 = 38
if num_1 < num_2:
  num = num_1
else:
  num = num_2
for i in range(2, num + 1):
  if num_1 % i == 0 and num_2 % i == 0:
    print(i)

print('========================')

n = 10
fib_1 = 1
fib_2 = 1
for i in range(3, n + 1):
  fib = fib_1 + fib_2
  fib_1 = fib_2
  fib_2 = fib
else:
  print(fib)

print('========================')

number = 15
for i in range(1, 10 + 1):
  print(number, 'X', i, '=', number * i)
