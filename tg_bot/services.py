import random
import time
from datetime import datetime

import xlsxwriter

from raw_orm import get_all_roles_id, last5_users



    
def _str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return datetime.fromtimestamp(ptime)


def random_date():
    return _str_time_prop("1/1/1971", "1/1/2015", '%d/%m/%Y', random.random())
    

def get_random_role_id():
    return random.choice(get_all_roles_id())['id']


def get_xlsx_name(chat_id):
    file_name = f'xlsx/last5_users_{chat_id}.xlsx'
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    colums = ["ФИО","Дата рождения","Наименование роли",]

    for i, v in enumerate(colums):
        worksheet.write(0, i, v)
        worksheet.write(0, i, v)
        worksheet.write(0, i, v)

    row = 1
    col = 0

    for user in last5_users():
        worksheet.write(row, col, user['fio'])
        worksheet.write(row, col+1, datetime.strptime(user['datar'],'%Y-%m-%d').strftime('%d-%m-%Y'))
        worksheet.write(row, col+2, user['name'])
        row += 1


    workbook.close()

    return file_name

