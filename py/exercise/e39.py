# import re
# pattern = re.compile('\d+')

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[1][1:-1]
  level1 = info[2][1:-1]
  if level0 in students:
    if level1 in students[level0]:
      students[level0][level1] += 1
    else:
      students[level0][level1] = 1
  else:
    students[level0] = {}
    students[level0][level1] = 1
print(students)

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[0][1:-1]
  level1 = info[3][1:-1]
  if level0 in students:
    if level1 in students[level0]:
      students[level0][level1] += 1
    else:
      students[level0][level1] = 1
  else:
    students[level0] = {}
    students[level0][level1] = 1
print(students)

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[0][1:-1]
  level1 = info[4][1:-1]
  if level0 in students:
    if level1 in students[level0]:
      students[level0][level1] += 1
    else:
      students[level0][level1] = 1
  else:
    students[level0] = {}
    students[level0][level1] = 1
print(students)

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[0][1:-1]
  level1 = info[2][1:-1]
  if level0 in students:
    if level1 in students[level0]:
      students[level0][level1] += 1
    else:
      students[level0][level1] = 1
  else:
    students[level0] = {}
    students[level0][level1] = 1
print(students)

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[1][1:-1]
  level1 = info[4][1:-1]
  if level0 in students:
    if level1 in students[level0]:
      students[level0][level1] += 1
    else:
      students[level0][level1] = 1
  else:
    students[level0] = {}
    students[level0][level1] = 1
print(students)

students = {}
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  level0 = info[0][1:-1]
  level1 = info[2][1:-1]
  level2 = '>90' if int(info[-3][1:-1]) > 90 else '<= 90'
  if level0 in students:
    if level1 in students[level0]:
      if level2 in students[level0][level1]:
        students[level0][level1][level2] += 1
      else:
        students[level0][level1][level2] = 1
    else:
      students[level0][level1] = {}
      students[level0][level1][level2] = 1
  else:
    students[level0] = {}
    students[level0][level1] = {}
    students[level0][level1][level2] = 1

import pprint
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(students)

import re
pattern = re.compile('\d\d\d')
secret = pattern.findall('2 x 2 = 4')
print(secret)

sm = 0
qt = 0

import collections
f = open('StudentsPerformance.csv')
c = collections.Counter()
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  c[info[0][1:-1]] += 1
  if info[0][1:-1] == 'male':
    sm += int(info[-2][1:-1])
    qt += 1
print(dict(c), sm, qt, sm / qt)


math_max = 0
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  math = int(info[-3][1:-1])
  if math > math_max: math_max = math
print('math', math)

qt = 0
reading = 0
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  math = int(info[-3][1:-1])
  if math < math_max: continue
  reading += int(info[-2][1:-1])
  qt += 1
print(reading, qt, reading / qt )

  # if math > math_max: math_max = math

qt = 0
writing = 0
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  lunch = info[3][1:-1]
  if lunch != 'free/reduced': continue
  qt += 1
  writing += int(info[-1][1:-2])
print(writing, qt, writing / qt)


#   info = line.split(',')
#   c[info[0][1:-1]] += 1
#   if info[0][1:-1] == 'male':
#     sm += int(info[-2][1:-1])
#     qt += 1
# print(dict(c), sm, qt, sm / qt)
