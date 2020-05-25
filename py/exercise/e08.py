#!/usr/bin/python3

OurBestStudents = ['Александр', 'Константин', 'Мария', 'Диана', 'Алексей',
                   'Максим', 'Светлана', 'Арина', 'Серафим', 'Doomer',
                   'Павел', 'Виктория', 'Елена', 'Галина', 'Вячеслав']

print('========================')

my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
new_list = my_list[::2]
result = 0
for number in new_list:
    result += number
print(result)

print('========================')

my_list = [1]
for i in range(10):
    my_list.append(my_list[i] * 2)
my_list.sort(reverse = True)
print(my_list)

print('========================')

fruits = 'яблоко банан апельсин баклажан перец помидор арбуз ананас'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
my_list.sort()
print(my_list)

print('========================')

result = 0
my_list = list()
for i in range(1, 50 + 1):
  if i % 3 == 0:
    my_list.append(i)
    result += i

print(result, my_list)

print('========================')

raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']

my_list = list()
for i in raw_list:
  my_list.append(len(i))
result = min(my_list) + max(my_list)

print(result, my_list)

print('========================')

raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
x_min = min(raw_list)
x_max = max(raw_list)
my_list = list()
for i in raw_list:
  if i % 2 == 0:
    my_list.append(i * x_min)
  else:
    my_list.append(i * x_max)
result = max(my_list)

print(result, my_list, raw_list)

# for i, number in enumerate(raw_list):
  # print(i, number)
  # if ()
  # my_list.append(i * x_min)

my_list = []
for x in range(1, 50):
  if x%7 == 0:
    my_list.append(x**0.5)
print(my_list)

my_list = [x ** 0.5 for x in range(1, 50) if x % 7 == 0]
print(my_list)


my_list = []
for x in range(90, 100):
    first_digit = x//10
    last_digit = x%10
    my_list.append(first_digit + last_digit)
print(my_list)
my_list = [x // 10 + x % 10 for x in range(90, 100)]
print(my_list)

phones = []
phones = ['+79033923029', '+78125849204', '+79053049385', '+79265748370', '+79030598495' ]
employee_base = {
    'Мария Никитина': '+79033923029',
    'Егор Савичев': '+78125849204',
    'Александр Пахомов': '+79053049385',
    'Алина Егорова': '+79265748370',
    'Руслан Башаров': '+79030598495',
}
employee_base = {'Мария Никитина': 'менеджер', 'Егор Савичев': 'разработчик', 'Александр Пахомов': 'дизайнер', 'Алина Егорова': 'разработчик', 'Руслан Башаров': 'верстальщик'}

spent = {
  '2019-04-01': 2504,
  '2019-04-02': 4994,
  '2019-04-03': 6343,
}
sum = 0
for v in spent.values():
  sum += v
print(sum)

results = [
  {'cost': 98, 'source': 'vk'},
  {'cost': 153, 'source': 'yandex'},
  {'cost': 110, 'source': 'facebook'},
]
result = -1
for rec in results  :
  if result == -1 or result > rec['cost']:
    result = rec['cost']
print(result)

defect_stats = [
  {'step number': 1, 'damage': 0.98},
  {'step number': 2, 'damage': 0.99},
  {'step number': 3, 'damage': 0.99},
  {'step number': 4, 'damage': 0.96},
  {'step number': 5, 'damage': 0.97},
  {'step number': 6, 'damage': 0.97},
]
val = 1
for rec in defect_stats:
  val *= rec['damage']
  if val < .9:
    print(rec['step number'])
    break

currency = {
  'AMD': {
    'Name': 'Армянских драмов',
    'Nominal': 100,
    'Value': 13.121
  },

  'AUD': {
    'Name': 'Австралийский доллар',
    'Nominal': 1,
    'Value': 45.5309
  },

  'INR': {
    'Name': 'Индийских рупий',
    'Nominal': 100,
    'Value': 92.9658
  },

  'MDL': {
    'Name': 'Молдавских леев',
    'Nominal': 10,
    'Value': 36.9305
  },
}
result = ''
result_rate = -1
for cur, rec in currency.items():
  rate = rec['Value'] / rec['Nominal']
  if result_rate == -1 or result_rate > rate:
    result_rate = rate
    result = cur
print(result)

bodycount = {
  'Проклятие Черной жемчужины': {
    'человек': 17
  },

  'Сундук мертвеца': {
    'человек': 56,
    'раков-отшельников': 1
  },

  'На краю света': {
    'человек': 88
  },

  'На странных берегах': {
    'человек': 56,
    'русалок': 2,
    'ядовитых жаб': 3,
    'пиратов зомби': 2
  }
}
result = 0
for rec in bodycount.values():
  for key, val in rec.items():
    # if key == 'человек' or key == 'пиратов зомби':
      result += val
print(result)



