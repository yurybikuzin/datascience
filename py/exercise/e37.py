bachelor_count = 0
f = open('StudentsPerformance.csv')
# for line in f:
for num, line in enumerate(f, 1):
  rec = line.split(',')
  if ('bachelor' in rec[2]):
    bachelor_count += 1
print(bachelor_count)

import collections
c = collections.Counter()

f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  rec = line.split(',')
  c[rec[2]] += 1

print(len(c.keys()), c.keys())

c = collections.Counter()
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  rec = line.split(',')
  c[rec[3]] += 1
print(len(c.keys()), dict(c))


c = collections.Counter()
f = open('StudentsPerformance.csv')
for num, line in enumerate(f, 0):
  if num == 0: continue
  rec = line.split(',')
  c[rec[1]] += 1
print(len(c.keys()), dict(c))

math = []

f = open('StudentsPerformance.csv')

# for line in f:
# info = []
c = collections.Counter()
for num, line in enumerate(f, 0):
  if num == 0: continue
  info = line.split(',')
  # if info[0] == '"gender"':
  #     continue
  # else:
  mark = int(info[5][1:-1])
  c[mark] += 1
  math.append(mark)
math_avg = sum(math)/len(math)
print(math_avg, dict(c))

above_avg = 0
for mark in math:
    if mark > math_avg:
        above_avg += 1
print(above_avg / 1000)

# ====

import re
pattern = re.compile('\d+')

exams = []
f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        new_line = []
        for item in info:
            if pattern.search(item) != None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])
        exams.append(new_line)
# print(exams)

reading_sum = 0
for line in exams:
  reading_sum += line[-2]
reading_avg = reading_sum / len(exams)
print(reading_avg)

reading_below_avg_count = 0
for line in exams:
  if line[-2] < reading_avg: reading_below_avg_count += 1
print(reading_below_avg_count)

reading_sum = 0
reading_base = 0
for line in exams:
  if line[0] == 'female':
    reading_base += 1
    reading_sum += line[-2]
reading_avg = reading_sum / reading_base
print(reading_avg)


c = collections.Counter()
writing_result = 0
writing_lunch = 0
# for num, line in enumerate(exams):
#   if num > 5: break
#   print(line)
for line in exams:
  if line[-1] > 90:
    writing_result += 1
    c[line[3]] += 1
    if line[3] == 'standard':
      writing_lunch += 1
print(dict(c)['standard']/ writing_result, dict(c), writing_result )


