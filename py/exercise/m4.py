import numpy as np

# ======================================================

if False:
  A = np.array([
    [0, -1, 1],
    [-1, 0, 1],
    [1, 1, 0],
  ])
  b = np.array([0, 0, 10])
  print(A, b)
  print(np.linalg.matrix_rank(A))
  Ab = np.c_[A, b]
  print(Ab)
  print(np.linalg.matrix_rank(Ab))
  if (np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab)):
    Ainv = np.linalg.inv(A)
    print(Ainv)
    w = np.dot(Ainv,b)
    print('ANSWER:', list([round(wi,2) for wi in w]))

# ======================================================

# Задание 4.2.2
# Найдите квадрат расстояния от точки (2;1) до прямой x + y = 1  с помощью метода Лагранжа
# f(x,y) = (x - 2)^2 + (y - 1)^2
# g(x,y) = x - y - 1 = 0
# L(x,y,l) = (x - 2)^2 + (y - 1)^2 + l(x + y - 1)
# dL/dx = 2(x-2) + l = 0
# dL/dy = 2(y-1) + l = 0
# dL/dl = x + y - 1 = 0
# 2x + 0y + l = 4
# 0x + 2y + l = 2
# 1x + 1y + 0l = 1
#      2 0 1       4
# A =  0 2 1  b =  2
#      1 1 0       1

if False:
  A = np.array([
    [2, 0, 1],
    [0, 2, 1],
    [1, 1, 0],
  ])
  b = np.array([4, 2, 1])
  print(A, b)
  print(np.linalg.matrix_rank(A))
  Ab = np.c_[A, b]
  print(Ab)
  print(np.linalg.matrix_rank(Ab))
  if (np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab)):
    Ainv = np.linalg.inv(A)
    print(Ainv)
    w = np.dot(Ainv,b)
    print('w:', w)
    # v = w - np.array([2, 1, 2])
    # print('v:', v)
    x = w[0]
    y = w[1]
    xy = np.array([x, y])
    M = np.array([2, 1])
    print('ANSWER:', (x - 2)**2 + (y - 1)**2, '==', np.linalg.norm(xy - M, 1))

# ======================================================

# Задание 4.2.3
# Прямоугольный параллелепипед имеет объем 1 м3. Какова минимальная площадь его поверхности?

# f(x,y,z)=2xy+2xz+2yz g(x,y,z)=x*y*z-1=0
# L(x,y,z,l) = 2xy+2xz+2yz+l(xyz - 1)
# dL/dx=2y+2z+lyz
# dL/dy=2x+2z+lxz
# dL/dz=2x+1y+lxy
# dL/dl=xyz-1
# 0x + 2y + 2z + lyz = 0
# 2x + 0y + 2z + lxz = 0
# 2x + 2y + 0z + lxy = 0
# xyz = 1
# 0x/z + 2y/z + 2 + 2y = 0

# ======================================================

# 4.3. Метод Лагранжа. Ограничения ─ неравенства

# Задача: У вас есть 20 метров забора, можно им огородить любой прямоугольник.
# Какую максимальную площадь можно огородить? Хотя бы одна сторона должна быть не меньше 6.

# max(f):f=x1*x2, 2*x1+2*x2=20, x1 >= 6
# min(f):f=-x1*x2, 2*x1+2*x2=20, -x1 + 6 + xt^2 = 0
# L(x1,x2,xt,l1,l2) = -x1*x2 + l1*(x1+x2-10) + l2*(-x1+6+xt^2)
# dL/dx1 = -x2 + l1 - l2
# dL/dx2 = -x + l1
# dL/dxt = 2*l2*xt
# dL/dl1 = x1+x2-10
# dL/dl2 = -x1+6+xt^2

# ======================================================

# Задание 4.3.3

# На стороне BC равностороннего треугольника ABC найти точку E такую, для которой параллелограмм ADEF,
# у которого точки D и F лежат соответственно на сторонах AB и AC, имеет наибольшую площадь.
# Сторона треугольника равна 1. Чему равна эта площадь c точностью до сотых?

# Высота ABC = 1/2*3**1/2


# ======================================================


if False:
  # Допустим, у нас есть n товаров с заданными стоимостями vi и массой wi.
  # В сумку убирается с кг.
  # Сколько какого товара взять, чтобы сумма всех стоимостей товаров была наибольшей?
  v = [4, 2, 1, 7, 3, 6] # values
  w = [5, 9, 8, 2, 6, 5] # weights
  C = 15
  n = 6
  # max(Sum(vi*xi)), Sum(wi*xi)
  # или
  # min(c.T@x), A@x<=b
  # где c = -v, A = w.T, b = (C)
  c = -np.array(v)
  A = np.array(w)
  print('A', np.shape(A), A)
  A = np.expand_dims(A, 0)
  print('A', np.shape(A), A)
  b = np.array([C])
  print('b', b)
  from scipy.optimize import linprog
  result = linprog(c=c,A_ub=A,b_ub=b)
  print(result)

  import cvxpy
  x = cvxpy.Variable(shape=n, integer=True)
  constraint = (A @ x <= b)
  total_value = c * x
  problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=[constraint])
  print('problem.solve', problem.solve())
  print('x.value', x.value)

  x = cvxpy.Variable(shape=n, integer=True)
  constraint = (A @ x <= b)
  x_positive = x >= 0
  total_value = c * x
  problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=[constraint, x_positive])
  print('problem.solve', problem.solve())
  print('x.value', x.value)

  x = cvxpy.Variable(shape=n, boolean=True)
  constraint = (A @ x <= b)
  x_positive = x >= 0
  total_value = c * x
  problem = cvxpy.Problem(cvxpy.Minimize(total_value), constraints=[constraint, x_positive])
  print('problem.solve', problem.solve())
  print('x.value', x.value)

# ======================================================

if False:
  Stock = np.array([180, 220])
  Store = np.array([110, 150, 140])
  Price = np.array([
    [2, 5, 3],
    [7, 7, 6],
  ])
  PricePlain = Price.flatten()

  import cvxpy as cp
  CarryPlain = cp.Variable(shape=6, integer=True)
  objective = cp.Minimize(cp.sum(PricePlain * CarryPlain))
  print(objective)
  Stock0_constraint = (CarryPlain[0] + CarryPlain[1] + CarryPlain[2]) == Stock[0]
  Stock1_constraint = (CarryPlain[3] + CarryPlain[4] + CarryPlain[5]) == Stock[1]
  Store0_constraint = (CarryPlain[0] + CarryPlain[3]) == Store[0]
  Store1_constraint = (CarryPlain[1] + CarryPlain[4]) == Store[1]
  Store2_constraint = (CarryPlain[2] + CarryPlain[5]) == Store[2]
  CarryPlain_positive = CarryPlain >= 0
  problem = cp.Problem(objective, constraints=[CarryPlain_positive, Stock0_constraint, Stock1_constraint, Store0_constraint, Store1_constraint, Store2_constraint])
  print('min', round(problem.solve()))
  Carry = np.reshape(
    np.array(list([round(x) for x in CarryPlain.value])),
    (2,3)
  )
  print('Carry:')
  print(Carry)

if False:
  Price = np.array([
    [1000, 12, 10, 19, 8],
    [12, 1000, 3, 7, 2],
    [10, 3, 1000, 6, 20],
    [19, 7, 6, 1000, 4],
    [8, 2, 20, 4, 1000],
  ])
  rows = Price.shape[0]
  cols = Price.shape[1]
  PricePlain = Price.flatten()
  # print(PricePlain.size)
  import cvxpy as cp
  AppointmentPlain  = cp.Variable(shape=PricePlain.size, integer=True)
  print('AppointmentPlain', AppointmentPlain)
  objective = cp.Minimize(cp.sum(PricePlain*AppointmentPlain))
  print('objective', objective)
  constraints = []
  for i in range(0, cols):
    # value_to_be_constrained = None
    # for j in range(0, rows):
    #   if value_to_be_constrained is None:
    #     value_to_be_constrained = AppointmentPlain[i*rows + i]
    #   else:
    #     value_to_be_constrained = value_to_be_constrained + AppointmentPlain[i*rows + i]
    # print('value_to_be_constrained', value_to_be_constrained)
    # constraints.append(value_to_be_constrained == 1)
    # print('constraints', constraints)

    constraints.append(
      (
        AppointmentPlain[0 + i] +
        AppointmentPlain[5 + i] +
        AppointmentPlain[10 + i] +
        AppointmentPlain[15 + i] +
        AppointmentPlain[20 + i]
      ) == 1
    )
  for i in range(0, rows):
    constraints.append(
      (
        AppointmentPlain[i*rows + 0] +
        AppointmentPlain[i*rows + 1] +
        AppointmentPlain[i*rows + 2] +
        AppointmentPlain[i*rows + 3] +
        AppointmentPlain[i*rows + 4]
      ) == 1
    )
  constraints.append(AppointmentPlain >= 0)
  problem = cp.Problem(objective, constraints=constraints)
  print('solution(min):', round(problem.solve()))
  Appointment = np.reshape(
    np.array(list([round(x) for x in AppointmentPlain.value])),
    (rows,cols)
  )
  print('Appointment:')
  print(Appointment)

if False:
  RouteCost = np.array([
  #   A   B   C   D   E
    [ 1000, 12, 10, 19,  8], # A
    [12,  1000,  3,  7,  8], # B
    [10,  3,  1000,  6, 20], # C
    [19,  7,  6,  1000,  4], # D
    [ 8,  8, 20,  4,  1000], # E
  ])
  rows = RouteCost.shape[0]
  cols = RouteCost.shape[1]
  RouteCostPlain = RouteCost.flatten()
  import cvxpy as cp
  RoutePlain = cp.Variable(shape=RouteCostPlain.size, integer=True)
  objective = cp.Minimize(cp.sum(RouteCostPlain*RoutePlain))
  constraints = []
  for i in range(0, cols):
    constraints.append(
      (
        RoutePlain[0 + i] +
        RoutePlain[5 + i] +
        RoutePlain[10 + i] +
        RoutePlain[15 + i] +
        RoutePlain[20 + i]
      ) == 1
    )
  for i in range(0, rows):
    constraints.append(
      (
        RoutePlain[i*rows + 0] +
        RoutePlain[i*rows + 1] +
        RoutePlain[i*rows + 2] +
        RoutePlain[i*rows + 3] +
        RoutePlain[i*rows + 4]
      ) == 1
    )
  constraints.append(RoutePlain >= 0)
  problem = cp.Problem(objective, constraints=constraints)
  print('solution(min):', round(problem.solve()))
  Route = np.reshape(
    np.array(list([round(x) for x in RoutePlain.value])),
    (rows,cols)
  )
  print('Route:')
  print(Route)

if False:
  # f(x,y,z) = 2*x^2-4*x*z+4*y^2-8*y*z+9*z^2+4*x+8*y-20*z
  # X[n+1]=X[n]-gamma*grad(f(X[n]))
  # https://lms2.sseu.ru/courses/eresmat/course1/razd12z1/par12_6z1.htm
  # grad(f(x,y,z)) = (
  #   4*(x-z+1), # https://allcalc.ru/node/663
  #   8*(y-z+1), # https://allcalc.ru/node/663
  #   -2*(2*x+4*y-9*z+10), # https://allcalc.ru/node/663
  # )
  def grad(P):
    x = P[0]
    y = P[1]
    z = P[2]
    return np.array([
       4*(x-z+1), # https://allcalc.ru/node/663
       8*(y-z+1), # https://allcalc.ru/node/663
       -2*(2*x+4*y-9*z+10), # https://allcalc.ru/node/663
    ])
  P = np.array([0, 0, 0])
  gamma = 0.25
  print(','.join(list([str(round(x)) for x in P - gamma * grad(P)])))

# ======================================================


# f(x,y) = (1-x)^2+100*(y-x^2)^2
# grad(f(x,y)) = [
#   2*(200*x^3-200*x*y+x-1),
#   200*(y-x^2),
# ]
if False:
  def grad(p):
    x = p[0]
    y = p[1]
    return np.array([
      2*(200*x**3-200*x*y+x-1), # https://allcalc.ru/node/663
      200*(y-x**2), # https://allcalc.ru/node/663
    ])

  gamma = 0.000001
  x_cur = np.array([0, 0])
  i = 0
  while True:
    x_cur = x_cur - gamma * grad(x_cur)
    i += 1
    if i % 100000 == 0: print(i, x_cur)
    if i >= 50000000: break

if False:
  from scipy import optimize
  def f(x, y):
    return 2*x**2-4*x*y+y**4+2
  print(optimize.minimize(lambda x: f(*x), x0=(2,1)))
  print(f(1,1))

if False:
  def f(w0, w1, w2):
    return (2.1 - w0 - w1)**2 + (2.9 - w0 - 3*w1)**2 + (4.1 - w0 - 5*w1)**2
  from scipy import optimize
  print(optimize.minimize(lambda p: f(*p), x0=(0,0,0)))
  print(optimize.minimize(lambda p: f(*p), x0=(1,1,1)))
  print(optimize.minimize(lambda p: f(*p), x0=(-1,-1,-1)))

if False:
  from scipy import optimize
  def f(x, y, z):
    return x**3-2*x**2+y**2+z**2-2*x*y+x*z-y*z+3*z
  print(optimize.minimize(lambda p: f(*p), x0=(1000,1000,1000)))
  # print(f(1,1))

if False:
  x_prev = np.array([0,0,0])
  x_curr = np.array([1,2,-5])
  gamma = 0.25
  alpha = 1
  # f(x,y,z) = 2*x^2-4*x*z+4*y^2-8*y*z+9*z^2+4*x+8*y-20*z
  # grad(f(x,y,z)) = [ # https://allcalc.ru/node/663
  #    4*(x-z+1),
  #    8*(y-z+1),
  #    -2*(2*x+4*y-9*z+10),
  # ]
  def grad(p):
    x = p[0]
    y = p[1]
    z = p[2]
    return np.array([
      4*(x-z+1),
      8*(y-z+1),
      -2*(2*x+4*y-9*z+10),
    ])
  x_next = x_curr - gamma*grad(x_curr) + alpha*(x_curr - x_prev)
  print(','.join([str(round(x)) for x in x_next]))

if True:
  def f(p):
    x = p[0]
    y = p[1]
    return x**2+x*y-2*x+3*y-1
  p_curr = np.array([0, 1])
  def grad(p):
    x = p[0]
    y = p[1]
    return np.array([
      2*x+y+2,
      x+3,
    ])
  H = np.array([
    [ 2,  1],
    [ 1 , 0]
  ])
  Hinv = np.linalg.inv(H)
  # # def H(p):
  # #   return np.array([
  # #     [ 2,  1],
  # #     [ 1 , 0]
  # #   ])
  # def Hinv(p):
  #   return np.linalg.inv(H(p))
  def F(p):
    x = p[0]
    y = p[1]
    return np.array([
      []
    ])
  print('p_curr', p_curr)
  print('H', H)
  print('Hinv', Hinv)
  print('grad(p_curr)', grad(p_curr))
  print('Hinv(p_curr)@grad(p_curr)', Hinv@grad(p_curr))
  print('p_curr - Hinv(p_curr)@grad(p_curr)', p_curr - Hinv@grad(p_curr))
  p_next = p_curr - Hinv@grad(p_curr)
  print('p_next', p_next)








# ======================================================
