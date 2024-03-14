import requests
from bs4 import BeautifulSoup
import math


def optimize_length(cell, word_length_slice):
    words = cell.split()
    new_cell = []

    for word in words:
        if len(word) <= word_length_slice:
            new_cell.append(word)
        else:
            if 'пр.' in word:
                new_cell.append(word[0:8] + '.')
            elif 'лаб.' in word:
                new_cell.append(word[0:9] + '.')
            else:
                new_cell.append(word[0:5] + '.')
    # print(new_cell)

    return ' '.join(new_cell)


def get_schedule(settings):
    link = settings['link']
    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')

    schedule_sheets = []
    for table in soup.find_all('table', border=True):
        schedule_sheet = []
        for tr in table.find_all("tr"):
            row = []
            for td in tr.find_all('td'):
                cell: str = td.text
                cell = cell.replace('\n', '')

                cell = optimize_length(cell, settings["word_length_slice"])

                # list_cell = list(cell)  #
                # for i in range(math.floor(len(cell) / white_space_treshold)):  #
                #     list_cell.insert(white_space_treshold * i, '\n')  #
                # cell = ''.join(list_cell)  #
                cell = cell.strip()
                row.append(cell)
            schedule_sheet.append(row)
        schedule_sheets.append(schedule_sheet)

    return schedule_sheets
