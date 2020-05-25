def get_median(lst):
  qt = len(lst)
  if qt % 2 == 1:
    result = lst[int((qt - 1) / 2)]
  else:
    result = (lst[int(qt / 2 - 1)] + lst[int(qt / 2)]) / 2
  return result
print(get_median([5, 2, 1, 3, 4]))
print(get_median([3, 3, 7, 9]))
    # lst[lst / 2]
# qt = 6
# if qt % 2 == 1:
#   print( int((qt - 1) / 2) )
# else:
#   print([int(qt / 2 - 1), int(qt / 2)])

user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]

# перепишите эту часть
def avg_orders(user_db):
  order_sum = sum([user['orders'] for user in user_db])
  orders_per_user = order_sum/len(user_db)
  return orders_per_user
orders_per_user = avg_orders(user_db)
print(orders_per_user)

all_the = sum
magic = range
print(all_the(magic(5)))

print(list(map(abs, [10,  -1, 42, -73]))[3])

word_sizes = list(map(len, ["all", "you", "need", "is", "map"]))
print(word_sizes)

values = [4, 8, 15, 16, 23, 42]
mean = 18

result = list(map(lambda x: x - mean, values))
print(result)

values = [4, 8, 15, 16, 23, 42]
mean = 18
result = list(filter(lambda x: x > mean, values))
print(result)

std = 42

def normalize(value):
    result = value/std
    return result

print(normalize(21))

std = 42

def normalize(value, std):
    result = value/std
    return result

print(normalize(21, 7))

values = [-7, -7, 7, 7]
std = 42

def count_std():
    mean = sum(values)/len(values)
    std = (sum([(value-mean)**2 for value in values])/len(values))**0.5
    return std

def normalize(value):
    result = value/std
    return result

print(normalize(21))

rabbits = 0

def count_rabbits(spotted):
    global rabbits
    rabbits += spotted


count_rabbits(3)
count_rabbits(5)
print(rabbits)

def normalize(numbers, mean=0, std=1):
  return list(map(lambda x: int((x - mean)/std),numbers))

print(normalize([10,20]))
print(normalize([10,20], std=2))
print(normalize([10,20], mean=15))

def sum_args(*args):
  result = 0
  for i in args:
    result += i
  return result

print(sum_args(1, 2, 3, 4, 5))

def show_keys(**kwargs):
    print(' '.join(kwargs.keys()))

show_keys(verbose=True, mode='constant')

def count_letters(string, average=False):
  words = string.split()
  result = 0
  for word in words:
    result += len(word)
  if average == False:
    return result
  elif len(word) > 0:
    return result / len(words)

print(count_letters('some   thing', average=True))
print(
  count_letters("Beep boop"),
  count_letters("Beep boop", average=True),
  count_letters("I will build my own theme park"),
  count_letters("I will build my own theme park", average=True),
)

words = ["sofa", "suitcase", "valise", "picture", "basket", "carton", "doggie"]
print(list(map(lambda w: sorted(w)[0], words))[5])

def always(n):
  return lambda:n
print(always(5)())
print(1548892800-1546300800, 86400*30)
print(7200/60)
