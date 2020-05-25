#!/usr/bin/python3
num_1 = 1812
num_2 = 2500
if num_1 < num_2:
  num = num_1
else:
  num = num_2
nod = 1
for i in range(2, int(num ** (1/2))):
  if num_1 % i == 0 and num_2 % i == 0:
    nod = i
if nod == 1:
  print("Общих делителей не найдено")
else:
  print(nod)

print('========================')

string = 'абстракция'
for i in string:
  if i in 'абв':
    continue
  print(i, end='')
print()

print('========================')

string = 'Нет'
for i in range(0, 5):
  if string == 'Да':
    print("Это отлично!")
    break
  else:
    print("Увы, это неправильный ответ")
else:
  print("Это безнадёжно!")


print('========================')

number = 173
for i in range(2, int(number ** (1/2)) + 1):
  if number % i == 0:
    print("Не является простым")
    break
else:
  print("Простое")

print('========================')

string = 'прелестная строка'
for i, letter in enumerate(string):
  if letter in 'аяоёыиуюэе' and i % 2 == 0:
    print("Строка мне не нравится!")
    break
else:
  print("Какая хорошая строка!")
