import numpy as np

# L = (2.1 - w0 - w1)^2 + (2.9 - w0 - 3w1)^2 + (4.1 - w0 - 5w1)^2
# dL/dw0 = 2*( -9.1 + 3w0 +  9w1)
# dL/dw1 = 2*(−31.3 + 9w0 + 35w1)
# grad(L) = [ dL/dw0, dL/dw1 ]
# grad(L) = 0 =>
#   [ dL/dw0, dL/dw1 ] = [ 0, 0 ] =>
#   [ -9.1 + 3w0 +  9w1 = 0, −31.3 + 9w0 + 35w1 = 0 ] =>
#   [ 3w0 +  9w1 = 9.1, 9w0 + 35w1 = 31.3 ] =>

if False:
  A=np.array([
    [3, 9] ,
    [9, 35]
  ])
  b=np.array( [9.1, 31.3] )
  print(A, b)
  print(np.linalg.matrix_rank(A))
  Ab=np.c_[A, b]
  print(Ab)
  print(np.linalg.matrix_rank(Ab))
  if (np.linalg.matrix_rank(A) == np.linalg.matrix_rank(Ab)):
    Ainv = np.linalg.inv(A)
    print(Ainv)
    w = np.dot(Ainv,b)
    print('ANSWER:', list([round(wi,2) for wi in w]))
    print('CHECK:', np.dot(A,w), '==', b)

# dL/dw0 = 2*( -9.1 + 3w0 +  9w1)
# dL/dw1 = 2*(−31.3 + 9w0 + 35w1)

# https://allcalc.ru/node/663
# d2L/dw0dw0 = 6
# d2L/dw0dw1 = 18
# d2L/dw1dw1 = 70
# d2L/dw1dw0 = 18

if False:
  Hesse = np.array([
    [5, 1], [1, 5]
  ])
  print(np.linalg.eig(Hesse))
  # this Hesse is positive determined => strict min

