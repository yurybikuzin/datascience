import pandas as pd
import numpy as np

if False:
  df = pd.DataFrame({'1.Rent': [65, 70, 120, 35, 40, 50, 100, 90, 85],
                                  '2.Area': [50, 52, 80, 33, 33, 44, 80, 65, 65],
                                  '3.Rooms':[3, 2, 1, 1, 1, 2, 4, 3, 2],
                                  '4.Floor':[5, 12, 10, 3, 6, 13, 8, 21, 5],
                                  '5.Demo two weeks':[8, 4, 5, 10, 20, 12, 5, 1, 10],
                                  '6.Liv.Area': [37, 40, 65, 20, 16, 35, 60, 50, 40]})
  def print_list(lst):
    print(','.join(map(lambda x: str(x), lst)))


  print(df.head())
  df['Rent-grivna'] = df['1.Rent'] / 10 * 4
  print(','.join(map(lambda x: str(int(x)), df['Rent-grivna'].tolist())))
  df['OneDemoDuration'] = [10, 20, 30, 15, 5, 40, 20, 8, 20]
  print(df.head())
  df['AllDemoDuration'] = df.OneDemoDuration * df['5.Demo two weeks']
  print(df.AllDemoDuration.sum())


  u=np.array([3,0,1,1,1])
  v=np.array([0,1,0,2,-2])
  w=np.array([1,-4,-1,0,-2])
  print('u*v', np.dot(u,v))
  print('v*w', np.dot(v,w))
  print('u*w', np.dot(u,w))
  lc = 2*v - 3*w
  print_list(lc.tolist())
  print('u*lc', np.dot(u,lc))
  print('|u|', np.linalg.norm(u), 'u1', u / np.linalg.norm(u))
  print('|v|', np.linalg.norm(v), 'v1', v / np.linalg.norm(v))
  print('|w|', np.linalg.norm(w), 'w1', w / np.linalg.norm(w))

  # import numpy as np

  Husband_Income=np.array([100,220,140])
  Wife_Income=np.array([150,200,130])
  Lover_Income=np.array([90,80,100])

  Husband_Сonsumption=np.array([50,50,60])
  Wife_Сonsumption=np.array([100,80,140])
  Lover_Сonsumption=np.array([100,20,140])
  Inc = np.array([
    Husband_Income,
    Wife_Income,
    Lover_Income,
  ]).T
  print(Inc)
  Cons = np.array([
    Husband_Сonsumption,
    Wife_Сonsumption,
    Lover_Сonsumption,
  ]).T
  print(Cons)
  NetInc = Inc * 0.87
  print(NetInc)
  print_list(NetInc[0].tolist())
  Balance = NetInc - Cons
  print(Balance)

  A = np.array([
    [1, 1],
    [2, -1],
    [1, 2],
  ])
  print(np.dot(A,A.T))

  A=np.array( [ [5,-1,3,1,2] , [-2,8,5,-1,1] ] )
  x=np.array( [1,2,3,4,5] )
  print(np.dot(A, x))
  # print(np.dot(x, A))

  A=np.array( [ [1,9,8,5] , [3,6,3,2] , [3,3,3,3], [0,2,5,9], [4,4,1,2] ] )
  B=np.array( [ [1,-1,0,1,1] , [-2,0,2,-1,1] ] )
  print(np.dot(B, A))

  x=np.array([1,2,1,0,4])
  y=np.array([2,1,-1,1,0])
  z=np.array([-1,1,-1,0,0])
  A = np.array([
    x,
    y,
    z,
  ])
  print(np.dot(A,A.T))

  Count_DF = pd.DataFrame({'Женские стрижки': [10, 2, 12, 4, 6, 10, 22, 7],
                                  'Мужские стрижки': [5, 21, 12, 8, 25, 3, 1, 0],
                                  'Окрашивания':[12, 3, 0, 18, 27, 2, 4, 31],
                                'Укладка':[15, 25, 30, 14, 25, 17, 25, 31],
                                  'Уход':[10, 6, 4, 5, 18, 12, 20, 28]
                                  },
                                 index=['Аня', 'Борис', 'Вика', 'Галя', 'Дима', 'Егор', 'Женя','Юра'])
  Price_DF = pd.DataFrame({'Женские стрижки': [2, 1.8, 2, 1.8, 2.5, 5, 1.1, 4.5],
                                  'Мужские стрижки': [1.5, 2.5, 2, 1.2, 3.5, 5, 1, 4],
                                  'Окрашивания':[1, 1, 0, 2.8, 2, 3, 1.5, 2.5],
                                'Укладка':[0.8, 1, 0.5, 0.8, 1, 2, 0.5, 1],
                                  'Уход':[1, 1, 2, 2, 1.5, 2.5, 1.7, 2]
                                  },
                                 index=['Аня', 'Борис', 'Вика', 'Галя', 'Дима', 'Егор', 'Женя','Юра'])

  print_list((Price_DF.loc['Борис'] * Count_DF.loc['Борис']).tolist())
  com=np.array([0.2, 0.2, 0.3, 0.1, 0.1])
  print(np.dot(Price_DF * Count_DF, com))
  # print(np.dot(Price_DF.loc['Борис'], Count_DF.loc['Борис']))

  print(np.dot(Price_DF * Count_DF, np.ones(5) - com))

  A=np.array( [[ 8 , 6 ,11],[ 7 , 5 , 9],[ 6 ,10,  6]])
  print(np.linalg.inv(A))

  v1=np.array([ 9, 10,  7,  7,  9])
  v2=np.array([2, 0, 5, 1, 4])
  v3=np.array([4, 0, 0, 4, 1])
  v4=np.array([ 3, -4,  3, -1, -4])
  S = np.array([
    v1,v2,v3,v4
  ])

  print(np.linalg.matrix_rank(S))
  G = np.dot(S,S.T)
  print(round(np.linalg.det(G)))
  print(np.linalg.matrix_rank(G))

  print(np.linalg.matrix_rank(S))

  print(np.linalg.inv(G))

  A = np.array([
    [4, 7],
    [5, 10],
  ])
  b = np.array([20, 30])
  print(np.dot(np.linalg.inv(A), b))



  A = np.array([
    [4, 7, -1],
    [2, 1, 1],
  ])
  Ab = np.array([
    [4, 7, -1, 7],
    [2, 1, 1, 2],
  ])
  print(np.linalg.matrix_rank(A), np.linalg.matrix_rank(Ab))


  A = np.array([
    [4, 7, -1],
    [-4, 2, 5],
    [0, 9, 4],
  ])
  Ab = np.array([
    [4, 7, -1, 7],
    [-4, 2, 5, 3],
    [0, 9, 4, 10],
  ])
  print(np.linalg.matrix_rank(A), np.linalg.matrix_rank(Ab))

  b = np.array([1, 2, 2])
  A = np.array([
    [1, -5],
    [2, 1],
    [1, 1],
  ])
  w = np.array([1, 1])
  e = b - np.dot(A,w)
  print(e)


  b = np.array([1, 4, 5, 0])
  A = np.array([
    [1, 2],
    [-3, 1],
    [1, 2],
    [1, -1],
  ])

  G = np.dot(A.T, A)
  print(G)
  Ginv = np.linalg.inv(G)
  print(Ginv)
  ATb = np.dot(A.T, b)
  print(ATb)
  ols = np.dot(Ginv, np.dot(A.T, b))
  print(ols)

  CRIM = 0.2
  RM = 6
  print(-29.3 - 0.26 * CRIM + 8.4 * RM)

  A = np.array([
    [1, -1, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 0, 2],
  ])
  G = np.dot(A.T, A)
  print(np.linalg.matrix_rank(G))

  x = np.array([11, 8])
  x = x - x.mean()
  x = x / np.linalg.norm(x)
  print(x)

df = pd.read_csv('Admission_Predict_Ver1.1.csv')
print(df.info(), df.head())
df = df.drop(['Serial No.'], axis=1)
print(df.info(), df.head())
# df = df.drop(['None'], axis=1)
print(df.info(), df.head()
  , df.columns
  )
if False:
  AdmitChance = df['Chance of Admit '].to_numpy()
  for i in ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']:
    np_factor = df[i].to_numpy()
    print(i, np.corrcoef([
      AdmitChance,
      np_factor,
    ]))
if False:
  for j in [0, 1]:
    AdmitChance = df[df.Research == j]['Chance of Admit '].to_numpy()
    for i in ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA']:
      np_factor = df[df.Research == j][i].to_numpy()
      print(j, i, np.corrcoef([
        AdmitChance,
        np_factor,
      ]))
if False:
  for j in [0]:
    AdmitChance = df[df.Research == j]['Chance of Admit '].to_numpy()
    for i in ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA']:
      np_factor = df[df.Research == j][i].to_numpy()
      print(j, i, np.corrcoef([
        AdmitChance,
        np_factor,
      ]))

# print()
if False:
  A=np.array([
    df[df.Research == 0]['TOEFL Score'].to_numpy(),
    df[df.Research == 0]['CGPA'].to_numpy(),
  ]).T
  print(A)
  b = df[df.Research == 0]['Chance of Admit '].to_numpy()
  print(b)
  print(np.dot(A.T, A))
  print(np.linalg.inv(np.dot(A.T, A)))
  print(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T))
  ols = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), b)
  print(ols)
  print(np.dot([107, 9.1], ols))


def _std(x):
  x = x - x.mean()
  x = x / np.linalg.norm(x)
  return x
if False:
  A=np.array([
    _std(df[df.Research == 0]['TOEFL Score'].to_numpy()),
    _std(df[df.Research == 0]['CGPA'].to_numpy()),
  ]).T
  print(A)
  b = _std(df[df.Research == 0]['Chance of Admit '].to_numpy())
  print(b)
  print(np.dot(A.T, A))
  print(np.linalg.inv(np.dot(A.T, A)))
  print(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T))
  ols = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), b)
  print([round(x, 2) for x in ols.tolist()])

# if True:
#   TOEFL = df[df.Research == 0]['TOEFL Score'].to_numpy()
#   TOEFL_c = TOEFL - TOEFL.mean()

#   CGPA = df[df.Research == 0]['CGPA'].to_numpy()
#   CGPA_c = CGPA - CGPA.mean()

#   y_c = y - y.mean()

#   TOEFL_st = TOEFL_c / np.linalg.norm(TOEFL_c)

#   CGPA_st = CGPA_c / np.linalg.norm(CGPA_c)

#   y_st = y_c / np.linalg.norm(y_c)

#   A_st=np.column_stack(( TOEFL_st, CGPA_st))

#   w_hat_st = np.linalg.inv(A_st.T@A_st)@A_st.T@y_st.values

#   w_hat_st

if False:
  v = np.array([1, 2, 3])
  F = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, -1, 0],
  ])
  print(np.dot(F, v))

if False:
  u = np.array([1, -1])
  v = np.array([1, 1])
  F = np.array([
    [2, 1],
    [1, 2],
  ])
  print(F@u)
  print(F@v)
  print(u + v)
  print(F@(u + v))
  print(5*u)
  print(F@(5*u))

if False:
  u = np.array([-1, 1])
  v = np.array([1, 1])
  F = np.array([
    [7, 2],
    [1, 8],
  ])
  print(F@u)
  print(F@v)

if False:
  P = np.array([
    [1, 1],
    [2, 1]
  ])
  D = np.array([
    [5, 0],
    [0, -1],
  ])
  print(P@D@np.linalg.inv(P))

if True:
  A = np.array([
    [5, 1],
    [1, 5],
  ])
  D = np.array([
    [6, 0],
    [0, 4],
  ])
  P = np.array([
    [1, -1],
    [1, 1],
  ])
  print('A', P@D@np.linalg.inv(P))
  P = np.array([
    [0, 4],
    [2, 4],
  ])
  print('A', P@D@np.linalg.inv(P))
  P = np.array([
    [4, 0],
    [4, 2],
  ])
  print('A', P@D@np.linalg.inv(P))

if False:
  A = np.array([
    [2, 1],
    [1, 5],
  ])
  result = np.linalg.eig(A)
  D = np.array([
    [result[0][0], 0],
    [0, result[0][1]],
  ])
  print(result[1])
  P = result[1]
  print('A', P@D@np.linalg.inv(P))

if False:
  r = 5
  C = np.array([
    [1, r],
    [r, 1],
  ])
  print(np.linalg.eig(C))
  print(np.linalg.inv(C)*-0.04166667)

if True:
  CRIM = np.array([0.00632, 0.02731, 0.02729, 0.03237, 0.06905, 0.02985, 0.08829])
  NOX = np.array([0.538, 0.469, 0.469, 0.458, 0.458, 0.458, 0.524])
  DIS = np.array([4.0900, 4.9671, 4.9671, 6.0622, 6.0622, 6.0662, 5.5605 ])
  C = np.corrcoef([NOX, DIS])
  print(C)
  print(np.linalg.eig(C))
  NEWFACTOR = 1 * _std(NOX) - 1 * _std(DIS)
  print(NEWFACTOR)
  NEWFACTOR_ST = _std(NEWFACTOR)
  print(NEWFACTOR_ST)

if True:
  C = np.array([
    [1, 0.8],
    [0.8, 1],
  ])
  print(np.linalg.eig(C))

if True:
  x1 = np.array([1, 2, 1, 1])
  x2 = np.array([70, 130, 65, 60])
  C = np.corrcoef([x1, x2])
  print([round(x, 4) for x in np.linalg.eig(C)[0]])
  print(round(np.linalg.cond(C), 4))
  xk = (0.70710678 * _std(x1) + 0.70710678 * _std(x2)) / (2 ** 0.5)
  print([round(x, 4) for x in xk])



# print(x)
# print(x.mean())
# x = x - x.mean()
# print(x)
# print(np.linalg.norm(x))
# x = x / np.linalg.norm(x)
# print(x)


# print(_std(df[df.Research == 0]['TOEFL Score'].to_numpy()))



# GREScore = df['GRE Score'].to_numpy()
# Research = df['Research'].to_numpy()
# # # print(df2)
# print(np.corrcoef([
#   AdmitChance,
#   GREScore,
# ]))
# print(np.corrcoef([
#   AdmitChance,
#   Research,
# ]))
# print(np.corrcoef([
#   GREScore,
#   Research,
# ]))

# print(np.corrcoef(df[[
#   'Chance of Admit ',
#   'GRE Score',
#   'Research',
# ]].to_numpy()))

