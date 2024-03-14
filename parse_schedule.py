import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import math


def get_schedule(settings):
    link = settings['link']
    req = requests.get(link)
    white_space_treshold = settings['white_space_treshhold']

    soup = BeautifulSoup(req.content, 'html.parser')

    schedule_sheets = []
    for table in soup.find_all('table', border=True):
        schedule_sheet = []
        for tr in table.find_all("tr"):
            row = []
            for td in tr.find_all('td'):
                cell: str = td.text
                cell = cell.replace('\n', '')

                list_cell = list(cell)                                                 #
                for i in range(math.floor(len(cell) / white_space_treshold)):          #
                    list_cell.insert(white_space_treshold * i, '\n')           #
                cell = ''.join(list_cell)                                              #

                cell = cell.strip()

                row.append(cell)
            schedule_sheet.append(row)
        schedule_sheets.append(schedule_sheet)

    return schedule_sheets


def format_schedule_sheet(schedule_sheet):
    result = ""

    str_rows = ['|' for i in range(len(schedule_sheet[0]))]
    str_caps = ['+' for i in range(len(schedule_sheet[0]))]

    for column in range(len(schedule_sheet[0])):
        longest_str = 3
        for row in range(len(schedule_sheet)):
            longest_str = max(longest_str, len(schedule_sheet[row][column]))
            # print(schedule_sheet[row][column])

        for row in range(len(schedule_sheet)):
            cell = schedule_sheet[row][column].center(longest_str)


            str_rows[row] += cell + '|'

            str_caps[row] += '-' * len(cell) + '+'

    for num, str_row in enumerate(str_rows[:-1]):
        result += str_caps[num] + '\n'
        result += str_row + '\n'
    result += str_caps[0]

    return result
