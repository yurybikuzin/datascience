# -*- coding: utf-8 -*-
import re
pattern = re.compile('[А-Я][а-я]*\W')
string = '!!! Йо! Учиться, учиться и учиться! Вперёд! Только вперёд!'
# print(pattern.match(string))
# print(pattern.search(string))
# print(pattern.findall(string))

text = 'Разработка языка Python была начата в конце 1980-х годов сотрудником голландского института CWI Гвидо ван Россумом. Для распределённой ОС Amoeba требовался расширяемый скриптовый язык, и Гвидо начал писать Python на досуге, позаимствовав некоторые наработки для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. Название языка произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х "Летающий цирк Монти Пайтона".'

print(re.compile('\d+').search(text))
print(re.compile('[A-Za-z]+').search(text))
print(re.compile('[А-Яа-я]+ка').search(text))
print(re.compile('[а][А-Яа-яЁё]{2}[и]').findall(text))
# print(re.compile('[аяоёыиуюэе]\W', re.IGNORECASE).findall(text))
print(len(re.compile('[аяоёыиуюэе]\s+[бвгджзйклмнпрстфхцчшщ]', re.IGNORECASE).findall(text)))


