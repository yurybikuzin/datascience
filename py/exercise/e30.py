proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
new_proverb = ''
proverb_even = proverb[0::2]
proverb_odd = proverb[1::2]
for i in range(0, max(len(proverb_even), len(proverb_odd))):
  new_proverb += (proverb_odd[i] if i < len(proverb_odd) else '') + proverb_even[i]
print(new_proverb)


# for i in range(0,len(proverb) + 1):
  # new_proverb


# print(len(proverb), int(len(proverb) / 2) + 1)

# basic_word =
basic_word = 'программирование'
inverted_word = ''
for i in range(len(basic_word) - 1, -1, -1):
  inverted_word += basic_word[i]
if basic_word == inverted_word:
  print('Слово "{}" является палиндромом'.format(basic_word) )
else:
  print('Слово "{}" - это не палиндром'.format(basic_word) )

proverbs = ['Без труда не вытянешь и рыбку из пруда',
            'Терпение и труд всё перетрут',
            'Работа не волк - в лес не убежит',
            'Чем труднее дело, тем выше честь',
            'Учиться, учиться и учиться!']

counter = 0
for proverb in proverbs:
    if 'труд' in proverb:
        counter += 1
print(counter)


# proverb = 'Хорошо написанная программа - это программа, написанная 2 раза'

# while True:
#     index = proverb.find('программа')
#     if index == -1:
#         break
#     secret = proverb[:index].split()[-1]
#     print(index, proverb[:index])
#     proverb = proverb[index+9:]
# print(secret, proverb)
email = 'yury.bikuzin@gmail.com'
print(email[email.find('@') + 1:])

number = 56.257
s = str(number)
result = 0
for i in range(s.find('.')+1, len(s)):
  result += int(s[i])
print(result)
  # print(int(s[i]))

emails_list = ['vasya@mail.ru',
        'akakiy@yandex.ru',
        'spyderman@yandex.ru',
        'XFiles@gmail.com',
        'hello@mail.ru',
        'noname@gmail.com',
        'DonaldTrump@mail.ru',
        'a768#af@yandex.ru',
        'Ivan_Ivanovich@yandex.ru',
        'thebestmail@yandex.ru']
import collections
c = collections.Counter()
for email in emails_list:
  c[email[email.find('@') + 1:]] += 1
emails_dict = dict(c)
print(emails_dict)

# emails_dict = {}
string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
secret = string[24:30]
new_string = string.replace(secret.lower(), secret.upper())
print(new_string)
print(secret)

string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
for delim in [':', '.', ',', '-', '!', '?']:
  string = string.replace(delim, ':)')
print(string)

name = 'Севастиан'
vowels = 'аяоёыиуюэе'
for i in range(0, len(name)):
  if name[i].lower() in vowels:
    print('{} - гласная буква'.format(name[i]))
  else:
    print('{} - согласная буква'.format(name[i]))


