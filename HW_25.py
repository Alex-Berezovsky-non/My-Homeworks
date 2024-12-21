from marvel import full_dict
from pprint import pprint

# Функция для ввода пользователя и обработки строки
def get_user_input() -> list[int | None]:
    """
    Запрашивает у пользователя цифры через пробел,
    преобразует их в список целых чисел, заменяя нечисловые значения на None.
    """
    user_input = input("Введите цифры через пробел: ")
    user_ids = user_input.split()
    return list(map(lambda x: int(x) if x.isdigit() else None, user_ids))

