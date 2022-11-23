"""
Задача 2
"""
import sys
from datetime import datetime
from typing import Callable


def timed_output(function: Callable) -> Callable:
    """декоратор, который добавляет в каждую строку вывода временную мету"""
    original_write = sys.stdout.write
    new_line_flag = True

    def my_write(string_text: str):
        nonlocal new_line_flag
        now = f'[{datetime.now():%Y-%m-%d %H:%M}]: '
        if new_line_flag:
            string_text = f'{now}{string_text}'
            new_line_flag = False
        if string_text == '\n':
            new_line_flag = True
        else:
            string_text = string_text.replace('\n', f'\n{now}')
        return original_write(string_text)

    def wrapper(name: str):
        sys.stdout.write = my_write
        return_value = function(name)
        sys.stdout.write = original_write
        return return_value

    return wrapper


if __name__ == '__main__':

    @timed_output
    def print_greeting(name):
        print(f'Hello, {name}!')

    print_greeting("Nikita")

    @timed_output
    def print_tests(name: str):
        """ещё тесты"""
        print(f'Hello, {name}!')
        print('')
        print(1, 2, 3)
        print('1, 2, 3,\n4, 5, 6')
        print(1, 2, 3, 4, 5, 6, sep='\n')

    print_tests("Nikita")
