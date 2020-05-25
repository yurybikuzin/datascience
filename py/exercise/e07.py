Y = 170000
Z = 1000000
year = 0
while Y < Z:
  Y *= 1.1
  year += 1
else:
  print(year)

print('========================')

weight = 77
weight_total = 0
weight_lim = 400
while True:
  weight_total += weight
  if weight_total > weight_lim:
    print("Перевес", weight_total - weight_lim, "кг")
    break

print('========================')

current_health = 500
attack = 80
secs = 0
while current_health > 0:
  current_health -= attack
  secs += 1
else:
  print(secs)

print('========================')

spent = 2800
balance = 10000
while balance >= 0:
  balance -= spent
  if balance > 0:
    print(balance)
else:
  print("Слишком большие расходы")


print('========================')

volume = 1000
dec = 5
step = 0
while volume >= 0:
  volume -= dec
  dec += 5
  step += 1
else:
  print(step)



