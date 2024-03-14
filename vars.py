styles = '''
"plain"
"simple"
"github"
"grid"
"simple_grid"
"rounded_grid"
"heavy_grid"
"mixed_grid"
"double_grid"
"fancy_grid"
"outline"
"simple_outline"
"rounded_outline"
"heavy_outline"
"mixed_outline"
"double_outline"
"fancy_outline"
"pipe"
"orgtbl"
"asciidoc"
"jira"
"presto"
"pretty"
"psql"
"rst"
"mediawiki"
"moinmoin"
"youtrack"
"html"
"unsafehtml"
"latex"
"latex_raw"
"latex_booktabs"
"latex_longtable"
"textile"
"tsv"'''

default_settings = """{
  "link": "https://kuzstu.ru/web-content/sitecontent/studentu/raspisanie/ПИб-232.html",
  "style": "double_grid",
  "maxcolwidth": 12,
  "word_length_slice": 10
}"""

no_schedule = 'Нет расписания для этой недели'

args_error = 'Ошибка аргументов. Используйте -h'


man = """Если ~/.config/kuz/settings.json не существует то используются стандартные настройки
Для корректной работы нужно в ~/.config/kuz/settings.json указать ссылку на страницу с расписанием КузГТУ
-с                         создать файл с настройками в домашней папке
-w N                       показать расписание для N недели
--help styles, -h styles   вывод списка стилей таблицы
--help, -h                 справка
"""


