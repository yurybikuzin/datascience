#!/usr/bin/python
# -*- coding: utf-8 -*-
pushkin_list = u"Мороз и солнце день чудесный еще ты дремлешь друг прелестный пора красавица проснись открой сомкнутой негой взоры".split(" ")

result = pushkin_list[5:10]
for i in result:
  print(i.encode("utf8"))
