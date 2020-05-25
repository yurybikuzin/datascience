import pandas as pd

# header = None — загрузить без строки с заголовком,
# skiprows=n — пропустить n строк (часто у документов бывает техническая «шапка»),
# encoding — загрузить в конкретной кодировке,
# na_values — список значений, который нужно заменить на NaN, специальный объект, обозначающий пропущенное значение.

if False:
  log = pd.read_csv('log.csv')

if False:
  log = pd.read_csv('log.csv', header=None)
  print(log.info(), log.head())

if False:
  sample = pd.read_csv('sample.csv')
  sample.columns = map(lambda x: x.lower(), sample.columns.tolist())
  columns = sample.columns
  # print(columns)
  print(sample.info(), sample.head(100))
  sample2 = sample[sample.age < 30]
  print(sample2.info(), sample2.head(100))

if False:
  log = pd.read_csv('log.csv', header=None)
  log.columns = ['user_id', 'time', 'bet', 'win']
  print(log.info(), log.head(30))
  print(log.user_id.unique())

if False:
  users = pd.read_csv('users.csv', encoding='koi8-r', sep='\t')
  users.columns = ['user_id', 'email', 'geo']
  print(users.info(), users.head())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time', 'bet','win']
  win_count = log[log.win.notnull()].win.count()
  print(win_count)

if False:
  sample = pd.read_csv("sample.csv")
  sample2 = sample[(sample.Age < 30) & (sample.Profession == 'Рабочий')]
  print(sample2.info(), sample2.head())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time', 'bet','win']
  log2 = log.query('bet < 2000 & win > 0')
  print(log2.info(), log2.head())

if False:
  sample = pd.read_csv("sample.csv")
  sample3 = sample[sample.City.str.match("о", na=False)]
  print(sample3.info(), sample3.head())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time', 'bet','win']
  new_log = log[~log.user_id.str.contains('error')]
  print(new_log.info(), new_log.head())

if False:
  sample = pd.read_csv("sample.csv")
  print(sample.info(), sample.head(100))
  sample2 = sample
  sample2.Age = sample.Age.apply(lambda x: x + 1)
  print(sample2)

if False:
  sample = pd.read_csv("sample.csv")
  sample2 = sample
  sample2.City = sample.City.apply(lambda x: str(x).lower())
  print(sample2)

def profession_code(s):
  if s == 'Рабочий': return 0
  if s == 'Менеджер': return 1
  return 2

if False:
  sample = pd.read_csv("sample.csv")
  sample2 = sample
  sample2.Profession = sample.Profession.apply(profession_code)
  print(sample2)

def age_category(age):
  if age < 23: return 'молодой'
  if age < 35: return 'средний'
  return 'зрелый'

if False:
  sample = pd.read_csv("sample.csv")
  sample['Age_category'] = sample.Age.apply(age_category)
  # sample2.Profession = sample.Profession.apply(profession_code)
  print(sample)

import unittest
class TestCase(unittest.TestCase):
  def test_clean_user_ud(self):
    self.assertEqual(clean_user_id("Запись пользователя № - user_974"), 'user_974')
    self.assertEqual(clean_user_id("#error"), '')

def clean_user_id(user_id):
  prefix = 'Запись пользователя № - '
  if (user_id.startswith(prefix)): return user_id[len(prefix):]
  if ('error' in user_id): return ''
  return user_id

if True:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time', 'bet','win']
  log.user_id = log.user_id.apply(lambda x: clean_user_id(str(x)))
  print(log.head())


def clean_time(t):
  if t.startswith('['): return t[1:]
  return t

if True:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  log.time = log.time.apply(lambda x: clean_time(str(x)))
  # t = log.time[0][1:]
  print(log.head())

if True:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  log = log[~log.user_id.str.contains('error')]
  log.user_id = log.user_id.apply(lambda x: clean_user_id(str(x)))
  log.time = log.time.apply(lambda x: clean_time(str(x)))


