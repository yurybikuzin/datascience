#!/usr/bin/python3
# -*- coding: utf-8 -*-

weight = 80
height = 1.8
print(weight / height ** 2)

a = 270
b = 12.8
print( ((a + b) / 2) ** (1/3) )

a = 23
print("Вы ввели число, которое при умножении на 3 даёт", a * 3)

string_1 = 'Hello, world!'
string_2 = 'Python <3'
string_3 = 'qwerty'
print((len(string_1) * len(string_2) * len(string_1)) ** (1/3))


string = 'Привет!'
power = 5
print(string, len(string), len(string) ** power)

word = 'ОченьДлинноеСлово'
if len(word) > 7:
  print("Это слово длинное.")
else:
  print("Это слово короткое.")

if 'ф' in word:
  print("Ого! Вы ввели редкое слово!")
else:
  print("Эх, это не очень редкое слово...")

letter = 'и'
if letter in word:
  print("Выбранная буква есть в введённом слове")
else:
  print("Выбранной буквы нет в введённом слове")

number = 169
result = number ** (1/2)
if result % 1 == 0:
  print(int(result))
else:
  print("Квадратный корень из", number, "- не целое число.")

number = 5
if number == 1:
  print('понедельник')
elif number == 2:
  print('вторник')
elif number == 3:
  print('среда')
elif number == 4:
  print('четверг')
elif number == 5:
  print('пятница')
elif number == 6:
  print('суббота')
elif number == 7:
  print('воскресенье')
else:
  print('Фигня какая-то')


weight = 80
height = 1.8
imt = weight / height ** 2
if imt < 18.5:
  print("Недостаточная масса тела")
elif imt > 24.99:
  print("Избыточная масса тела")
else:
  print("Норма")


mark = 7
if mark < 4:
  print("неудовлетворительно")
elif mark < 6:
  print("удовлетворительно")
elif mark < 8:
  print("хорошо")
else:
  print("отлично")

balance = 455
if balance > 5000:
  print("Сегодня твой выбор - ресторан!")
elif balance < 2500:
  print("Придётся потерпеть!")
else:
  print("Эх, только фастфуд")

number = 452
if number % 2 == 0:
  print("Число делится на 2 без остатка.")
elif number % 3 == 0:
  print("Число делится на 3 без остатка.")
elif number % 5 == 0:
  print("Число делится на 5 без остатка.")
else:
  print("Число не делится ни на 2, ни на 3, ни на 5 без остатка!")

print("239" < "30" and 239 > 30)
print(False and True or 12<5**2 and "Python" > "Ruby")
print("Android" > "Apple" or "Apple" > "Android")

x = 10
y = 15
print(y > x**y - 1000 or "test" > "push")

flower = 'роза'
color = 'фиолетовый'
if flower == 'роза' and (color == 'синий' or color == 'белый'):
  print("Ане понравятся эти цветы")
else:
  print("Аня не фанат таких цветов")

height = 180
weight = 92
color = 'синий'
if height > 170 and weight < 80 and color == 'red':
  print("Ваша половинка нашлась!")
else:
  print("Попробуем поискать ещё...")

number = 346
if number % 2 == 0 or number % 5 == 0 or number % 173 == 0 or number % 821 == 0:
  print("Вова, это нужное число")
else:
  print("Вова, в этот раз ты не попал")

fav_word = 'Аппликация'
if fav_word == "плюс" or fav_word == "плюсы":
  print("C++")
elif fav_word == "рубин" or fav_word == "кристалл":
  print("Ruby")
else:
  print("Python")

hour = 18
minute = 47
if (
    hour < 10 or
    hour == 10 and minute >= 30 or
    hour == 11 or
    hour == 13 and minute >= 40 or
    hour == 14 or
    hour == 18 or
    hour == 19 and minute <= 30 or
    hour >= 20
  ):
  print("Преподаватель занят.")
else:
  print("Преподаватель свободен.")

# if fav_word == "рептилия" or fav_word == "питон" or fav_word == "змея":
#   print()

word = 'подшипник'
for i, letter in enumerate(word):
  if i % 2 == 0:
    print(letter)

year_1 = 2013
year_2 = 2020
for i in range(year_1, year_2 + 1):
  if i % 4 == 0:
    print(i, "год високосный")
  else:
    print(i, "год невисокосный")

word = 'Зимушка-зима'
for i in word:
  if i in 'аяоёыиуюэе':
    print(i)

name = 'Сергей'
for i, letter in enumerate(name):
  print('Буква', i + 1, 'в этом имени -', letter)

num_1 = 25
num_2 = 45
if num_2 < num_1 or num_1 < 0:
  print("Введён неверный диапазон чисел")
else:
  for i in range(num_1, num_2 + 1):
    if (i % 3 == 0 or i % 5 == 0) and (i % 2 == 1):
      print(i)


