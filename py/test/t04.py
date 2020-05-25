#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
def count_a_words(s):
  return filter(lambda w: re.search(r'[Аа]', w), s.split(" "))

result = count_a_words(u"Мороз и солнце день чудесный еще ты дремлешь друг прелестный пора красавица проснись открой сомкнутой негой взоры")
# print(result)
for i in result:
  print(i)
  # print(i.encode("utf8"))

# print(re.search(ur'[Аа]', u'пора'))


