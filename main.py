import sys
import parse_schedule
from tabulate import tabulate
import json
from subprocess import Popen, PIPE


def getSettings():
    # cmd = ['pwd']
    # with Popen(cmd, stdout=PIPE) as proc:
    #     print(proc.stdout.read().decode('utf-8'))
    #
    # cmd = ['ls']
    # with Popen(cmd, stdout=PIPE) as proc:
    #     print(proc.stdout.read().decode('utf-8'))

    with open('/usr/local/bin/settings.json', 'r') as file:
        return json.loads(file.read())


args = sys.argv
settings = getSettings()

if len(args) <= 2 or args[1] in ['--help', '-h']:
    help = """Для получения расписания используйте аргумент -w и введите номер недели"""
    print(help)
    sys.exit()

if len(args) != 3:
    print('Arg error')
    sys.exit()
if args[1] != '-w':
    print('Arg error')
    sys.exit()
try:
    week_num = int(args[2])
except Exception as e:
    print('Arg error')
    sys.exit()

schedule = parse_schedule.get_schedule(settings)

if week_num <= 0 or week_num > len(schedule):
    print('Нет расписания для этой недели')
    sys.exit()

print(tabulate(schedule[week_num - 1], tablefmt=settings['style']))
