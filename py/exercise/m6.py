if False:
  import pandas as pd
  df = pd.read_csv('framingham.csv')
  print(df.info())
  df = df[
    pd.notnull(df['glucose']) &
    pd.notnull(df['education']) &
    pd.notnull(df['BPMeds']) &
    pd.notnull(df['cigsPerDay']) &
    pd.notnull(df['BMI']) &
    pd.notnull(df['totChol']) &
    pd.notnull(df['heartRate'])
  ]
  # print(df.info())
  print(df.diabetes.value_counts())
  print(round(99/3658, 3))
  print(df.prevalentStroke.value_counts())
  print(round(df[df['diabetes'] == 1].sysBP.mean(), 2))
  print(round(df[df['diabetes'] == 1].sysBP.median(), 2))

# print(df.diabetes.value_counts())

# print(df.head())
if False:
  import math
  def sigma(teta, x):
    assert(len(teta) == len(x) + 1)
    q = teta[0]
    for i in range(0, len(x)):
      q += teta[i + 1] * x[i]
    return 1/(1 + math.exp(-q))
    # len(teta), len(x)
    # print()

  # teta = [-0.51, 0.23, 0.1]
  teta = [-0.51, 0.23, 0.1]
  x = [0.3, 15]
  print(1 - sigma(teta, x))

if False:
  TP = 170
  FP = 20
  TN = 140
  FN = 10

  P = TP + FP
  Accuracy = (TP + TN)/(TP + FP + TN + FN)
  sensitivity = TP / (TP + FN)
  specificity = TN / (TN + FP)
  pricision = TP / (TP + FP)
  completeness = TP / (TP + FN)

  print('Positive:', P)
  print('Accuracy:', round(Accuracy, 2))
  print('sensitivity:', round(sensitivity, 2))
  print('specificity:', round(specificity, 2))
  print('pricision:', round(pricision, 2))
  print('completeness', round(completeness, 2))

if True:
  import pandas as pd
  from sklearn import linear_model
  from sklearn.linear_model import LogisticRegression
  from sklearn.model_selection import train_test_split
  from sklearn import metrics
  import matplotlib.pyplot as plt
  import seaborn as sn
  import matplotlib.mlab as mlab
  # %matplotlib inline

  df = pd.read_csv('framingham.csv')
  df.dropna(axis=0,inplace=True)
  print(df.columns)

  if False:
    dfx = df.drop('TenYearCHD', axis=1)
    dfy = df[['TenYearCHD']]
    # print(dfx.head())
    # print(dfy.head())
    X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.2)
    lm = linear_model.LogisticRegression(solver='liblinear')
    model = lm.fit(X_train, y_train.values.ravel())
    print(model.coef_)
    print(model.intercept_)
    print(X_test[:1])
    print(lm.predict_proba(X_test[:1]))
    print(lm.predict(X_test[:1]))
    y_pred = lm.predict(X_test)
    print(y_pred)
    print(y_pred.sum())
    print(lm.score(X_test, y_test))
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    print(y_test['TenYearCHD'].value_counts())
    print(y_pred.sum())
    sn.heatmap(cnf_matrix, annot=True)
    # plt.show(sn)

  if False:
    list_col=['age']
    dfx = df[list_col]
    dfy = df[['TenYearCHD']]
    X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.2)
    lm = linear_model.LogisticRegression(solver='liblinear')
    model = lm.fit(X_train, y_train.values.ravel())
    print(model.coef_)
    print(model.intercept_)
    print(X_test[:1])
    print(lm.predict_proba(X_test[:1]))
    print(lm.predict(X_test[:1]))
    y_pred = lm.predict(X_test)
    print(y_pred)
    print(y_pred.sum())
    print(lm.score(X_test, y_test))
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    # print(y_test['TenYearCHD'].value_counts())
    # print(y_pred.sum())
    # sn.heatmap(cnf_matrix, annot=True)

  if True:
    list_col=['cigsPerDay', 'diabetes', 'totChol', 'sysBP', 'BMI', 'glucose']
    dfx = df[list_col]
    dfy = df[['TenYearCHD']]
    X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.2)
    lm = linear_model.LogisticRegression(solver='liblinear')
    model = lm.fit(X_train, y_train.values.ravel())
    print(model.coef_)
    print(model.intercept_)
    print(X_test[:1])
    print(lm.predict_proba(X_test[:1]))
    print(lm.predict(X_test[:1]))
    y_pred = lm.predict(X_test)
    print(y_pred)
    print(y_pred.sum())
    print(lm.score(X_test, y_test))
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    print(y_test['TenYearCHD'].value_counts())
    print(4/104)
    print(629/630)

  if False:
    list_col=['male']
    dfx = df[list_col]
    dfy = df[['TenYearCHD']]
    X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.2)
    lm = linear_model.LogisticRegression(solver='liblinear')
    model = lm.fit(X_train, y_train.values.ravel())
    print(model.coef_)
    print(model.intercept_)
    print(X_test[:1])
    print(lm.predict_proba(X_test[:1]))
    print(lm.predict(X_test[:1]))
    y_pred = lm.predict(X_test)
    print(y_pred)
    print(y_pred.sum())
    print(lm.score(X_test, y_test))
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
    print(y_test['TenYearCHD'].value_counts())
    print(y_pred.sum())
    sn.heatmap(cnf_matrix, annot=True)



