class DepartmentReport():
  def add_revenue(self, amount):
    if not hasattr(self, 'revenues'):
      self.revenues = []
    self.revenues.append(amount)
  def average_revenue(self):
    if not hasattr(self, 'revenues'):
      return 0
    return sum(self.revenues) / len(self.revenues)


report = DepartmentReport()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# => [1000000, 400000]
print(report.average_revenue())
# => 700000.0


class DepartmentReport():
  def __init__(self, company_name):
    self.company_name = company_name
    self.revenues = []
  def add_revenue(self, amount):
    self.revenues.append(amount)
  def average_revenue(self):
    average_revenue = 0 if len(self.revenues) == 0 else round(sum(self.revenues) / len(self.revenues))
    return 'Average department revenue for {}: {}'.format(self.company_name, average_revenue)
    # if len(self.revenues) == 0:
    #   return 0
    # return sum(self.revenues) / len(self.revenues)

report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())

class User():
  def __init__(self, email, password, balance):
    self.email = email
    self.password = password
    self.balance = balance
  def login(self, email, password):
    return self.email == email and self.password == password
  def update_balance(self, delta):
    self.balance += delta


user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# => False
print(user.login("gosha@roskino.org", "qwerty"))
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700

import collections
class IntDataFrame():
  def __init__(self, lst):
    self.lst = list(map(lambda x: int(x), lst))
    self.c = collections.Counter()
  def count(self):
    return len(list(filter(lambda x: x != 0, self.lst)))
  def unique(self):
    for i in self.lst:
      self.c[i] += 1
    return len(self.c.keys())


df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.count())
# => 5
print(df.unique())
# => 4

class OwnLogger():
  def __init__(self):
    self.entries = []
  def log(self, message, level):
    self.entries.append({'message': message, 'level': level})
  def show_last(self, level = 'all'):
    lst = self.entries.copy()
    lst.reverse()
    for i in lst:
      if level == 'all' or i['level'] == level:
        return i['message']
  # def show_entries(self):
  #   lst = self.entries.copy()
  #   lst.reverse()
  #   print(lst)



logger = OwnLogger()
logger.log("System started", "info")
print(logger.show_last("error"))
# logger.show_entries()
# => None
# Некоторые интерпретаторы Python могут не выводить None, тогда в этой проверке у вас будет пустая строка
logger.log("Connection instable", "warning")
logger.log("Connection lost", "error")
# logger.show_entries()

print(logger.show_last())
# => Connection lost
print(logger.show_last("info"))
# => System started