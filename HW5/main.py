# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.

from datetime import datetime
from task1HW import get_hero_intel


def make_trace(log_path):

    def _make_trace(old_function):

        def new_function(*args, **kwargs):
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.now()} вызвана функция {old_function.__name__}')
                f.write(f'аргумены функции {args} {kwargs}')
                result = old_function(*args, **kwargs)
                f.write(f'возвращен результат {result}')
            return result

        return new_function

    return _make_trace

