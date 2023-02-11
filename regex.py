import re

# лекция
# text="Регулярное выражение - это шаблон, сопоставляемый с искомой строкой слева направо. Термин «Регулярное выражение» сложно произносить каждый раз, поэтому, обычно, вы будете сталкиваться с сокращениями 'регэкспы' или 'регулярки'."
# pattern = r'регулярн\w*\S+выражен\w*'
# result = re.findall(pattern, text, re.I) # ищем наш паттерн в тексте, регистрозависим, re.I - игнорирует регистр
# print(result)
#
# result = re.sub(pattern, "RegEx", text) # заменим паттерн на RegEx в тексте
# print(result)
#
# # либо
# pattern = re.compile(r'регулярн\w*\S+выражен\w*', flags=re.I)
# print(pattern.findall(text))

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
for page in contacts_list_new:
  page_string = ','.join(page) # объединение в строку
  format_page = re.sub(name_pattern, r'\1\3\10\4\6\9\7\8', page_string)
  page_list = format_page.split(',') # формируем список строк
  if page_list not in contacts_list:
    contacts_list.append(page_list)
pprint(contacts_list)

# дубликаты в одну

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
#
