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
# Функция для фильтрации словаря по введенным id
def filter_dict_by_ids(data: dict, ids: list[int | None]) -> dict:
    """
    Фильтрует словарь по переданным id.
    """
    return {id_: data[id_] for id_ in ids if id_ in data}
