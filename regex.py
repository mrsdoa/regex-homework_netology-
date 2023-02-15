import re
import numpy as np
# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf8") as f:
  rows = csv.reader(f, delimiter=',')
  contacts_list = list(rows)
# pprint(contacts_list)

pattern = r'(\+7|7|8)?(\s?|\(?)*(\d{3})(\s?|\)?)*[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})'
contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page)
  format_page = re.sub(pattern, r'+7(\3)\5-\6-\7', page_string)  # замена номеров в строке
  page_list = format_page.split(',')  # формируем список строк
  contacts_list_new.append(page_list)
  # print(page_list)

name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                   r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
contacts_list = list() # создаем список
for item in contacts_list_new:
  page_string = ','.join(item) # объединение в строку
  format_page = re.sub(name_pattern, r'\1\3\10\4\6\9\7\8', page_string)
  page_list = format_page.split(',') # формируем список строк
  if page_list not in contacts_list:
    contacts_list.append(page_list)
# pprint(contacts_list)

# дубликаты
for i in contacts_list:
  # print(i)
  for j in contacts_list:
    # print(j)
    if i[0] == j[0] and i[1] == j[1] and i != j:
      if i[2] == '':
        i[2] = j[2]
      if i[3] == '':
        i[3] = j[3]
      if i[4] == '':
        i[4] = j[4]
      if i[5] == '':
        i[5] = j[5]
      if i[6] == '':
        i[6] = j[6]
# print(len(contacts_list))

header = contacts_list[0]
body = contacts_list[1:]
s = []
for item in body:
  d = dict(zip(header, item))
  s.append(d)
# print(header)
# print(body)
# pprint(s)

# l = [{'a': 123, 'b': 1234},
#         {'a': 3222, 'b': 1234},
#         {'a': 123, 'b': 1234}]

seen = set()
new_l = []
for d in s:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)

final_ = []
final_.append(header)
for item in new_l:
  final_.append(list(item.values()))
pprint(final_)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(final_)
