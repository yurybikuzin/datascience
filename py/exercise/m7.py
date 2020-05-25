if False:
  lst = [1, 2, 3, 4, 5, 6]

  sma = []
  for i in range(1, len(lst)):
    sma.append(lst[i]*0.7+lst[i-1]*0.3)
    # sma.append((lst[i]+lst[i-1])/2)

  print(sma)

if False:
  lst = [1, 0, 1, -1, 2, 0, 1]

  sma = []
  for i in range(2, len(lst)):
    sma.append(lst[i]*0.5+lst[i-1]*0.3+lst[i-2]*0.2)
    # sma.append((lst[i]+lst[i-1])/2)
  print(sma)

if False:
  import pandas as pd

  df = pd.read_csv('solarpower_cumuldaybyday2.csv')
  # print(df.info())
  df['dt'] = pd.to_datetime(df['date']) #.apply(pd.datetools.normalize_date)
  df['week'] = df['dt'].dt.week
  # print(df.info())
  # # print(df.head())
  # # print(pd.to_datetime('2014-10-07').week)
  # print(df[df['week'] == 40].groupby('week').cum_power.sum())
  # print(df[df['week'] == 41].groupby('week').cum_power.sum())
  # print(df[df['week'] == 42].groupby('week').cum_power.sum())
  print(df.groupby('week').count())

if False:
  import pandas as pd
  from statsmodels.tsa.seasonal import seasonal_decompose
  from matplotlib import pyplot
  df = pd.read_csv('candy_production.csv')
  df = df.set_index(pd.DatetimeIndex(df['observation_date']))
  df.drop(['observation_date'], axis = 1, inplace = True)
  decomposition = seasonal_decompose(df, model='additive')
  decomposition.plot()
  pyplot.show()

  # trend_part = decomposition.trend # отдельно трендовая составляющаяя
  # seasonal_part = decomposition.seasonal # отдельно сезонная составляющаяя
  # residual_part = decomposition.resid # отдельно шум: то, что осталось
  # print(trend_part.info())
  # print(seasonal_part.info())
  # print(residual_part.info())

if False:
  import numpy as np
  from matplotlib import pyplot
  import statsmodels.api as sm
  mu = 0
  sigma = 1
  num = 100
  # print(np.random.normal(mu, sigma, size=num))
  # np.random.normal(mu, sigma, size=num)
  eps = np.random.normal(mu, sigma, size=num)
  walk = np.zeros(num)
  walk[0] = eps[0]
  walk[1] = eps[1]
  a = 0.2
  b = 0.1
  for i in range (2,num):
    walk[i] = a*walk[i-1] + b*walk[i-2] + eps[i]
  # pyplot.plot(range(0, num), walk)
  # pyplot.show()
  test = sm.tsa.adfuller(walk)
  print(test[1])


if True:
  import numpy as np
  from matplotlib import pyplot
  import statsmodels.api as sm
  mu = 0
  sigma = 1
  num = 100
  # print(np.random.normal(mu, sigma, size=num))
  # np.random.normal(mu, sigma, size=num)
  eps = np.random.normal(mu, sigma, size=num)
  walk = np.zeros(num)
  walk[0] = eps[0]
  walk[1] = eps[1]
  a = 0.9
  b = 0.07
  for i in range (2,num):
    walk[i] = a*walk[i-1] + b*walk[i-2] + eps[i]
  test = sm.tsa.adfuller(walk)
  print(test[1])
  pyplot.plot(range(0, num), walk)
  pyplot.show()


