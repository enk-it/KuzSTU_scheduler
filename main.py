#!/usr/bin/python
import sys
import parse_schedule
from tabulate import tabulate
from vars import default_settings, styles, no_schedule, args_error, man
import json
import os


def get_settings():
    path = os.path.expanduser('~') + "/.config/kuz/"
    filename = "settings.json"
    if os.path.exists(path + filename):
        with open(path + filename, 'r') as file:
            settings_str = file.read()
    else:
        settings_str = default_settings
    return json.loads(settings_str)


args = sys.argv

if len(args) < 2:
    print(args_error)
    sys.exit()

if args[1] == '-c':
    path = os.path.expanduser('~') + "/.config/kuz/"
    filename = "settings.json"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'w') as file:
        file.write(default_settings)
    print('Файл создан')
    sys.exit()

if args[1] == '-w':
    if len(args) != 3:
        print(args_error)
        sys.exit()
    try:
        week_num = int(args[2])
    except Exception as e:
        print(args_error)
        sys.exit()
    settings = get_settings()
    schedule = parse_schedule.get_schedule(settings)

    if week_num <= 0 or week_num > len(schedule):
        print(no_schedule)
        sys.exit()

    print(tabulate(schedule[week_num - 1], tablefmt=settings['style']))
    sys.exit()

if args[1] in ['--help', '-h']:
    if len(args) == 3 and args[2] == 'styles':
        print(styles)
    else:
        print(man)
    sys.exit()

print(args_error)
sys.exit()