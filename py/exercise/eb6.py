import pandas as pd

def clean_user_id(user_id):
  prefix = 'Запись пользователя № - '
  if (user_id.startswith(prefix)): return user_id[len(prefix):]
  if ('error' in user_id): return ''
  return user_id

def clean_time(t):
  if t.startswith('['): return t[1:]
  return t

def get_log():
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  # print(log.head())
  # log = log[~log.user_id.str.contains('error')]
  # log.user_id = log.user_id.apply(lambda x: clean_user_id(str(x)))
  # log.time = log.time.apply(lambda x: clean_time(str(x)))
  # print(log.head())
  return log

log = get_log()
# print(log.info(), log.head())
time = log.time.isna()
# print(log[log.user_id.str.contains('error')].head())
# print(log[log.time.isna()].head())
# print(time[time == True].count())
# print(time[time == True].head())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  print(log.info())
  log2 = log.dropna(axis=1)
  print(log.info(), log2.info())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  print(log.info())
  log2 = log.dropna(axis=0)
  print(log.info(), log2.info())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  print(log.info())
  # log2 = log.dropna(axis=0, subset=['user_id', 'time'])
  log2 = log.dropna(axis=1, subset=[2, 3])
  print(log.info(), log2.info())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  # print(log.info())
  log2 = log.drop_duplicates(subset=['user_id', 'time'])
  # log2 = log.dropna(axis=1, subset=[2, 3])
  print(log.info(), log2.info())

if False:
  log = pd.read_csv("log.csv",header=None)
  log.columns = ['user_id','time','bet','win']
  print(log.time.count())
  log = log.dropna(axis=0, subset=['time'])
  log.time = log.time.apply(lambda x: clean_time(str(x)))
  print(log.time.count())
  log.time = pd.to_datetime(log.time)
  # print(log.info())
  # log2 = log.drop_duplicates(subset=['user_id', 'time'])
  # log2 = log.dropna(axis=1, subset=[2, 3])
  # from datetime import strftime
  print(
  #   # log.info(), log.head(),
    log[log.time == log.time.max()].iloc[0].time,
    type(log[log.time == log.time.max()].iloc[0].time),
    log[log.time == log.time.max()].iloc[0].time.strftime('%Y-%m-%d')
  )

if False:
  log = pd.read_csv("log.csv")
  log = log.dropna()
  log.columns = ['user_id', 'time', 'bet', 'win']
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  # log['time'] = log['time'].dt.strftime('%M')
  # log['time'] = log.time.apply(lambda x: x.minute)
  log.time = log.time.apply(lambda x: x.minute)
  # Пропущенная строка
  # print('here')
  print(log['time'].head())

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  # log = log.dropna(axis=0, subset=['time'])
  log = log.dropna()
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  log['minute'] = log.time.apply(lambda x: x.minute)
  log['month'] = log.time.apply(lambda x: x.month)
  log['weekday'] = log['time'].dt.strftime('%w')
  log['dayperiod'] = log['time'].apply(lambda x: int(x.hour / 6))
  print(
    log.dayperiod.value_counts().head()
  )
  # print(log['minute'].value_counts().head())
  # print(log['month'].value_counts(ascending=True).head())
  # print(log['weekday'].value_counts(ascending=True).head(7))

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log = log.dropna()
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  log['hour'] = log['time'].apply(lambda x: x.hour)
  print(log.head())


if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  # log = log.dropna(axis=0, subset=['time'])
  # log['time'] = log['time'].apply(lambda x: x[1:])
  # log['time'] = pd.to_datetime(log['time'])
  # log['hour'] = log['time'].apply(lambda x: x.hour)
  log.bet = log['bet'].fillna(0)
  print(log.bet.value_counts())

def fillna_win(row):
  if not pd.isna(row.win): return row.win
  if row.bet == 0: return 0
  return -row.bet
  # print(pd.isna(row.win))
  # return row.win
# Нужно дописать
# Применяем функцию

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet
  print(log[log.net > 0].count())
  print(round(log[log.net > 0].net.mean()))
  print(round(log[log.net > 0].net.median()))
  # print(log.bet.count())
  # print(log[log.bet > 0].bet.sum())
  print(round(log[log.bet > 0].bet.count() / log.bet.count(), 3) * 100)
  print(log[log.bet > 0].bet.mean())
  print(log[(log.bet > 0)].net.mean())
  # print(log[(log.bet > 0) & (log.net < 0)].net.mean())
  print(log[(log.net < 0)].net.mean())
  print(log[(log.bet > 0) & (log.net > 0)].net.count())
  print(log[(log.bet > 0) & (log.net < 0)].net.count())

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  min_bet_amount = log[log.bet == log.bet.min()].bet.count()
  print(min_bet_amount)

if False:
  # Приведем признак user_id к одному формату в обоих датасетах
  # us = pd.read_csv('users.csv')
  #
  users = pd.read_csv('users.csv', encoding='koi8-r', sep='\t')
  users.columns = ['user_id', 'email', 'geo']
  users.user_id = users.user_id.apply(lambda x: x.lower())
  # Избавимся от ошибок в user_id

  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  # print(users.info(), users.head(), log.info(), log.head())
  merged = pd.merge(log, users, on='user_id')
  print(merged.info(), merged.head())
  print(merged.groupby('user_id').win.median().median())

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet
  print(log.head(10))
  print(log.groupby('user_id').net.sum())
  print('median', log.groupby('user_id').net.sum().median())


if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet
  users_bet = pd.DataFrame({ 'user_id': log[log.bet > 0].user_id.unique()})
  df = log[log.bet == 0].groupby('user_id').bet.count().to_frame()
  merged = users_bet.merge(df, on='user_id', how='left')
  print(users_bet.head())
  print(df.head())
  print(merged.bet.mean())
  # grouped = pd.DataFrame()
  # print(grouped.head())

if False:
  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet

  users_bet = pd.DataFrame({ 'user_id': log[log.bet > 0].user_id.unique()})
  first_visit = log.groupby('user_id').time.min().to_frame()
  bet_first_nonzero = log[log.bet > 0].groupby('user_id').time.min().to_frame()
  print(first_visit.info(), first_visit.head())
  print(bet_first_nonzero.info(), bet_first_nonzero.head())
  merged = users_bet.merge(first_visit, on='user_id', how='left')
  print(merged.info(), merged.head())
  merged = merged.merge(bet_first_nonzero, on='user_id', how='left')
  print(merged.info(), merged.head())
  merged['delta'] = merged.time_y - merged.time_x
  print(merged.info(), merged.head())
  print(merged.delta.mean())

if False:
  users = pd.read_csv('users.csv', encoding='koi8-r', sep='\t')
  users.columns = ['user_id', 'email', 'geo']
  users.user_id = users.user_id.apply(lambda x: x.lower())

  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet

  merged = users.merge(log, on='user_id', how='right')
  print(merged.groupby('geo').win.sum().sort_values(ascending=False).head())

if True:
  users = pd.read_csv('users.csv', encoding='koi8-r', sep='\t')
  users.columns = ['user_id', 'email', 'geo']
  users.user_id = users.user_id.apply(lambda x: x.lower())

  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  log['time'] = log['time'].apply(lambda x: x[1:])
  log['time'] = pd.to_datetime(log['time'])
  log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  log['net'] = log.win - log.bet

  merged = users.merge(log, on='user_id', how='right')
  bet_mean_by_geo = merged[merged.bet > 0].groupby('geo').bet.mean().sort_values(ascending=False)
  print(bet_mean_by_geo.iloc[0] / bet_mean_by_geo.iloc[bet_mean_by_geo.count() - 1])

if True:
  users = pd.read_csv('users.csv', encoding='koi8-r', sep='\t')
  users.columns = ['user_id', 'email', 'geo']
  users.user_id = users.user_id.apply(lambda x: x.lower())

  log = pd.read_csv("log.csv")
  log.columns = ['user_id', 'time', 'bet', 'win']
  log.bet = log['bet'].fillna(0)
  log = log[log.user_id != '#error']
  log.user_id = log.user_id.str.split(' - ').apply(lambda x: x[1])
  # log['time'] = log['time'].apply(lambda x: x[1:])
  # log['time'] = pd.to_datetime(log['time'])
  # log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
  # log['net'] = log.win - log.bet

  merged = users.merge(log, on='user_id', how='right')
  # print(merged.groupby('geo').time.count().sort_values(ascending=False).head())
  sample2 = merged.groupby('geo').time.count()
  print(sample2)
  # bet_mean_by_geo = merged[merged.bet > 0].groupby('geo').bet.mean().sort_values(ascending=False)
  # print(bet_mean_by_geo.iloc[0] / bet_mean_by_geo.iloc[bet_mean_by_geo.count() - 1])


