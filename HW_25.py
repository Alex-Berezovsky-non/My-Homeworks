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
# Функция для создания множества уникальных режиссеров
def get_unique_directors(data: dict) -> set[str]:
    """
    Создает множество уникальных значений ключа 'director'.
    """
    return {movie['director'] for movie in data.values()}

# Функция для создания копии словаря с годами в виде строк
def convert_years_to_strings(data: dict) -> dict:
    """
    Создает копию словаря, где значения ключа 'year' преобразованы в строки.
    """
    return {id_: {**movie, 'year': str(movie['year'])} for id_, movie in data.items()}
