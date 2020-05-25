
import numpy as np

if False:
  arr1 = np.array([1,2,3,4])
  arr2 = np.array([5,6,7,8], dtype = float)
  arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

  print(arr1)
  print(arr2.dtype)
  print(arr3)
  print(np.shape(arr3))

  import pandas as pd

  df = pd.DataFrame()
  x = df.values
  print(type(x))

  my_series = pd.Series([5, 6, 7, 8, 9, 10])
  print(my_series.values, type(my_series.values))


  print(np.empty(5)) # одномерный массив из пяти элементов, память для которого выделена, но не инициализирована
  print(np.zeros((10, 7))) # массив размером 10x7, заполненный нулями
  print(np.ones((3,3,3)) )# массив размером 3х3х3, заполненный единицами
  print(np.eye(3) )# единичная матрица (элементы главной диагонали равны 1, остальные — 0) размера 3х3
  print(np.full((3, 5), 3.14))  # массив 3x5 заполненный числом 3.14
  print(np.arange(0, 21, 7)  )# одномерный массив, заполненный числами в диапазоне от 0 до 20 с шагом 7
  print(np.linspace(0, 1, 5)  )# массив из пяти чисел, равномерно распределённых в интервале между 0 и 1 включительно
  print(np.random.randint(0, 10, (3, 3))  )# массив размера 3х3, заполненный случайными числами из диапазона от 0 до 10

  my_secret = [x for x in range(1, 301, 7) if x%10 == 7 or x%10 == 1]
  print(np.array([my_secret, [x/2 for x in my_secret], [x-100 for x in my_secret]]))

  print('-'*10)
  i = 0
  print(i, np.ones(5))
  i += 1
  # print(i, np.ones(5,5))
  i += 1
  print(i, np.ones((5,5)))
  i += 1
  print(i, np.eye(5))
  i += 1
  print(i, np.full((5,5), 1))
  i += 1
  print(i, np.array([[1,2,3,4,5], [5,1,2,3,4], [4,5,1,2,3], [3,4,5,1,2], [2,3,4,5,1]]))

  print('-'*10)
  i=0
  print(i, np.random.randint(0, 4, (3, 3)))
  i += 1
  print(i, np.random.randint(0, 5, (3, 3)))
  i += 1
  print(i, np.random.randint(0, 6, (3, 3)))
  i += 1
  print(i, np.random.randint(0, 5, 3))

  my_array = np.array([[1,2,3,4], [10,11,12,13], [45,46,47,48]])
  print(my_array[1:, 1:3])


first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])
acc = 0
for i in big_secret[:,-1]:
  acc += i
print(round(acc, 2))

m = big_secret[:,0:5]
shape = np.shape(m)
acc = 0
for i in range(0, min(shape[0], shape[1])):
  acc += m[i,i]
print(round(acc, 2))

m = big_secret[:,-5:]
shape = np.shape(m)
acc = 1
for i in range(0, min(shape[0], shape[1])):
  acc *= m[i,i]
print(round(acc, 2))

shape = np.shape(big_secret)
for i in range(0, shape[0]):
  for j in range(0, shape[1]):
    if i % 2 and j % 2:
      big_secret[i,j] = 1
    if i % 2 == 0 and j % 2 == 0:
      big_secret[i,j] = -1
print(big_secret)

m = big_secret[:,0:5]
shape = np.shape(m)
acc = 0
for i in range(0, min(shape[0], shape[1])):
  acc += m[i,i]
print(round(acc, 2))

m = big_secret[:,-5:]
shape = np.shape(m)
acc = 1
for i in range(0, min(shape[0], shape[1])):
  acc *= m[i,i]
print(round(acc, 2))

print('='*20)
a = np.array([3,6,9])
b = np.array([12,15,18])

result1 = a+b
result2 = b-a
result3 = a*b
result4 = a/b
result5 = a*2
print('Сумма: {}\nРазность: {}\nПроизведение: {}\nЧастное: {}\nУмножение на число: {}'.format(result1, result2, result3, result4, result5))

print(np.modf(big_secret))
print(np.abs(big_secret))
print(np.isnan(big_secret))

my_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(my_array.T)

my_array = np.random.randint(0, 10, 20)
print(my_array.reshape((4,5)))

my_array = np.array([[1,2,3], [11,22,33], [111,222,333]])
print(my_array.flatten())
print(my_array.reshape((9)))

my_array = np.random.randint(0, 10, (3,4))
print(my_array)
print(my_array<5)
print(my_array[my_array<5])
mask = np.array([1, 0, 1, 0], dtype=bool)
print(my_array[:, mask])
mask = np.array([True, False, True, False])
print(my_array[:, mask])
# for i

my_array = np.random.randint(0, 10, (4, 6))
print(my_array)
print(np.sort(my_array, axis=1))
print(np.sort(my_array, axis=0))

first = [x**(1/2) for x in range(100)]
second = [x**(1/3) for x in range(100, 200)]
third = [x/y for x in range(200,300,2) for y in [3,5]]

great_secret = np.array([first, second, third]).T
print(np.shape(great_secret))
# print(great_secret)
# great_secret_cos =
acc = 0
for i in np.cos(great_secret[0]):
  acc += i
print(round(acc, 2))

acc = 0
for i in great_secret[great_secret>50]:
  acc += i
print(acc)
print(great_secret.flatten()[150])
great_secret_sorted = np.sort(great_secret, axis=0)
# great_secret_sorted = np.sort(great_secret, axis=0)
# print(great_secret_sorted[-1,:], great_secret[-1,:])
acc = 0
for i in great_secret_sorted[-1,:]:
  acc += i
print(round(acc,2))

students = np.array([
  range(1,11),
  [135, 160, 163, 147, 138, 149, 136, 154, 137, 165],
  [34, 43, 40, 44, 41, 54, 39, 48, 35, 60],
  [4, 5, 4.3, 5, 4.7, 3.9, 4.2, 4.9, 3.7, 4.6],
]).T
print(students)
print(np.mean(students[:,-1]))
print(np.median(students[:,-1]))
print(np.median(students[:,-2]))
print(round(np.mean(students[:,-2]) - np.median(students[:,-2]), 1))

print(np.corrcoef(students[:,1], students[:,2]))
print(np.corrcoef(students[:,1], students[:,3]))
print(np.corrcoef(students[:,2], students[:,3]))
print(np.std(students[:,1]))
print(np.std(students[:,-1]))
print(np.std(students[:,-2])**2)
# for i in range
# for i in range()
my_array = np.array([[1,2,3,4,5],
                     [6,7,8,9,10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]])

my_sin = np.sin(my_array)
print(round(np.sum(my_sin), 3))
my_sin[1:4,1:4] = np.ones((3,3), dtype=int)
print(my_sin)
print(round(np.sum(my_sin), 3))
m = my_sin[:, 0:4].reshape((10,2))
print('m',m)
print('m',round(np.sum(m[:,0]), 3))

bigdata = np.array([x**2 for x in range(101,1000,2)], dtype=int)
print(np.median(bigdata))
print(round(np.std(bigdata), 0))
# print(len(bigdata))
print(len(bigdata[range(0,int(len(bigdata)/2) + 1,2)]))
print(len(bigdata[range(1,int(len(bigdata)/2) + 1,2)]))
print(np.corrcoef(
  bigdata[range(0,int(len(bigdata)/2) + 1,2)],
  bigdata[range(1,int(len(bigdata)/2) + 1,2)]
))
# print()

# print(round(np.sum(my_sin), 3))
