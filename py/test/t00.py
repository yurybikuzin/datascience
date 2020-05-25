import math
def calc_exp(a,b,c,d):
  return (math.sqrt(a + b) + math.sqrt(c + d)) / (a * a + c * c)
  # (2 + 3) / 2
print(calc_exp(1, 3, 1, 8))
# print(math.sqrt(4))
