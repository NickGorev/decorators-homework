"""
Задача 1
Для начала, давайте подменим метод write у объекта sys.stdout на такую функцию,
которая перед каждым вызовом оригинальной функции записи данных в stdout
допечатывает к тексту текущую метку времени.
"""
import sys
from datetime import datetime

original_write = sys.stdout.write
new_line_flag = True


def my_write(string_text: str) -> int:
    global new_line_flag
    now = f'[{datetime.now():%Y-%m-%d %H:%M}]: '
    if new_line_flag:
        string_text = f'{now}{string_text}'
        new_line_flag = False
    if string_text == '\n':
        new_line_flag = True
    else:
        string_text = string_text.replace('\n', f'\n{now}')
    return original_write(string_text)


sys.stdout.write = my_write

print('1, 2, 3')
print(1, 2, 3)
print('1, 2, 3,\n4, 5, 6')
print(1, 2, 3, 4, 5, 6, sep='\n')

sys.stdout.write = original_write
