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
# Функция для фильтрации фильмов, начинающихся на букву 'Ч'
def filter_movies_starting_with_ch(data: dict) -> dict:
    """
    Фильтрует фильмы, названия которых начинаются на букву 'Ч'.
    """
    return {id_: movie for id_, movie in data.items() if movie['title'] is not None and movie['title'].startswith('Ч')}

# Функция для сортировки словаря по году
def sort_dict_by_year(data: dict) -> dict:
    """
    Сортирует словарь по ключу 'year'.
    """
    return dict(sorted(data.items(), key=lambda x: int(x[1]['year']) if isinstance(x[1]['year'], str) and x[1]['year'].isdigit() else (x[1]['year'] if isinstance(x[1]['year'], int) else float('inf'))))
# Функция для сортировки словаря по году и названию
def sort_dict_by_year_and_title(data: dict) -> dict:
    """
    Сортирует словарь по двум ключам: 'year' и 'title'.
    """
    return dict(sorted(data.items(), key=lambda x: (
        int(x[1]['year']) if isinstance(x[1]['year'], str) and x[1]['year'].isdigit() else (x[1]['year'] if isinstance(x[1]['year'], int) else float('inf')),
        x[1]['title'] if x[1]['title'] is not None else ''
    )))

# Функция для однострочника: фильтрация и сортировка
def filter_and_sort_movies(data: dict) -> dict:
    """
    Фильтрует фильмы, названия которых начинаются на 'Ч', и сортирует их по году.
    """
    return dict(sorted(filter(lambda x: x[1]['title'] is not None and x[1]['title'].startswith('Ч'), data.items()), key=lambda x: (
        int(x[1]['year']) if isinstance(x[1]['year'], str) and x[1]['year'].isdigit() else (x[1]['year'] if isinstance(x[1]['year'], int) else float('inf')),
        x[1]['title'] if x[1]['title'] is not None else ''
    )))
# Основной код
if __name__ == "__main__":
    # 1. Получаем ввод пользователя
    user_ids = get_user_input()

    # 2. Фильтруем словарь по введенным id
    filtered_dict = filter_dict_by_ids(full_dict, user_ids)

    # 3. Создаем множество уникальных режиссеров
    unique_directors = get_unique_directors(full_dict)

    # 4. Преобразуем годы в строки
    year_as_string_dict = convert_years_to_strings(full_dict)

    # 5. Фильтруем фильмы, начинающиеся на 'Ч'
    starts_with_ch = filter_movies_starting_with_ch(full_dict)

    # 6. Сортируем словарь по году
    sorted_by_year = sort_dict_by_year(full_dict)

    # 7. Сортируем словарь по году и названию
    sorted_by_year_and_title = sort_dict_by_year_and_title(full_dict)

    # 8. Однострочник: фильтрация и сортировка
    filtered_and_sorted = filter_and_sort_movies(full_dict)

    # Красивый вывод результатов
    print("Задание 2: Словарь по введенным id")
    pprint(filtered_dict)

    print("\nЗадание 3: Уникальные режиссеры")
    pprint(unique_directors)

    print("\nЗадание 4: Годы как строки")
    pprint(year_as_string_dict)

    print("\nЗадание 5: Фильмы, начинающиеся на 'Ч'")
    pprint(starts_with_ch)

    print("\nЗадание 6: Сортировка по году")
    pprint(sorted_by_year)

    print("\nЗадание 7: Сортировка по году и названию")
    pprint(sorted_by_year_and_title)

    print("\nЗадание 8: Однострочник для фильтрации и сортировки")
    pprint(filtered_and_sorted)