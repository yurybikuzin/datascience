from copy import copy
import pdb

# def remove_dups(values):
#     values = copy(values)
#     for i in range(len(values)):
#         pdb.set_trace()
#         if i >= len(values) - 2: break
#         if values[i] in values[i+1:]:
#             values.remove(values[i])
#     return values

# print(remove_dups([1, 12, 4, 1, 4, 8]))
user_db = [
  {"name": "Elena", "age": 19, "salary": 80_000},
  {"name": "Sergey", "age": 31, "salary": 160_000},
  {"name": "Olga", "age": 33, "salary": 170_000},
  {"name": "Vadim", "age": 17, "salary": 45_000}
]

def group_values(db, value_key, group_key, step):
    # grouped = defaultdict(list)
    grouped = {}
    for item in db:
      key = int(item[group_key] / step) * step
      if not key in grouped:
        grouped[key] = []
      grouped[key].append(item[value_key])
    return grouped

print(group_values(user_db, "salary", "age", 10))

def safe_exec(fn):
  try:
    return fn()
  except Exception as e:
    print(e)
    return 0

def zero_div():
  return 5/0

safe_exec(zero_div)