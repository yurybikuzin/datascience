import numpy as np

if False:
  x = np.array([4, 5])
  y = np.array([2, 1])
  u = np.array([1, 0])
  print(2*x-3*y+5*u)

if False:
  m = np.array([3, 4, 5, 9])
  s = np.array([1, 5, 3, 6])
  print(s*400 - m*200)

if False:
  x = np.array([-1, -2])
  y = np.array([1, 2])
  M = np.array([x, y])
  print(np.linalg.matrix_rank(M))
  x = np.array([-3, -2])
  y = np.array([1, 1])
  u = np.array([4, 3])
  M = np.array([x, y, u])
  print(np.linalg.matrix_rank(M))
  x = np.array([-3, -2])
  y = np.array([1, 1])
  M = np.array([x, y])
  print(np.linalg.matrix_rank(M))

if True:
  v1=np.array([9, 10, 7, 7, 9])
  v2=np.array([2, 0, 5, 1, 4])
  v3=np.array([4, 0, 0, 4, 1])
  v4=np.array([3, -4, 3, -1, -4])
  M = np.array([v1, v2, v3, v4])
  print(np.linalg.matrix_rank(M))
  G = M @ M.T
  print(G)
  print(round(np.linalg.det(G)))
  Ginv = np.linalg.inv(G)
  print(round(Ginv[2][0], 3))
