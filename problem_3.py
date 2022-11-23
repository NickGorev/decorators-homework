"""
Задача 3
Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.
"""
import sys
import os
from typing import Callable


def redirect_output(filepath: str, *file_args, **file_kwargs) -> Callable:
    """
    генерирует декоратор, перенаправляющий вывод из stdout в файл filepath
    """
    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            with open(filepath, 'w', *file_args, **file_kwargs) as otf:
                sys.stdout = otf
                return_value = function(*args, **kwargs)
            sys.stdout = original_stdout
            return return_value
        return wrapper
    return decorator


if __name__ == '__main__':

    @redirect_output('./function_output.txt')
    def calculate():
        for power in range(1, 5):
            for num in range(1, 20):
                print(num ** power, end=' ')
            print()

    calculate()

    os.system('type function_output.txt')
