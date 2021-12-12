# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

header_list = contacts_list.pop(0)
book_string = ''

for row in contacts_list:
    book_string += ','.join(row) + '\n'
re_name_two = re.compile(r'^([А-Я][а-я]+)\s?([А-Я][а-я]+)\,{2}', re.MULTILINE)
re_name_three = re.compile(
    r'([А-Я][а-я]+)\s?\,?([А-Я][а-я]+)\s?\,?([А-Я][а-я]+)\,+')
re_phone = re.compile(
    r'(\+7|8)\s*\(?(\d{3})\)?\s*\-?(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
re_phone_add = re.compile(r'\(?доб\.?\s?(\d{4})?\)?')

book_string = re_name_two.sub(r'\1,\2,', book_string)
book_string = re_name_three.sub(r'\1,\2,\3,', book_string)
book_string = re_phone.sub(r'+7(\2)\3-\4-\5', book_string)
book_string = re_phone_add.sub(r'доб.\1', book_string)

tmp_list = book_string.split('\n')
tmp_list.remove('')

contacts_list_new_tmp = []

for el in tmp_list:
    contacts_list_new_tmp.append(el.split(','))

contacts_dict = {}

for contact in contacts_list_new_tmp:
    if contact[0] not in contacts_dict:
        contacts_dict[contact[0]] = contact
    else:
        for i in range(1, 7):
            if (contacts_dict[contact[0]][i] != contact[i] and
                    contacts_dict[contact[0]][i] == ''):
                contacts_dict[contact[0]][i] = contact[i]

contacts_list_new = []
for val in contacts_dict.values():
    contacts_list_new.append(val)
contacts_list_new.insert(0, header_list)
pprint(contacts_list_new)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
    datawriter.writerows(contacts_list_new)
