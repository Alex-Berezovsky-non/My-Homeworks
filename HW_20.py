# Задача 1

small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

search_term = input("Введите название фильма или его часть: ").lower()
found_movies = []

for title, year in small_dict.items():
    if search_term in title.lower():
        found_movies.append(title)

if found_movies:
    print("Найденные фильмы:")
    for movie in found_movies:
        print(movie)
else:
    print("Фильмы не найдены.")

    # Задача 2

filtered_titles = []
filtered_dict = {}
filtered_list_of_dicts = []

for title, year in small_dict.items():
    if year is not None and year > 2024:
        filtered_titles.append(title)
        filtered_dict[title] = year
        filtered_list_of_dicts.append({title: year})

# Задача 2.1
print("Фильмы, вышедшие после 2024 года:")
for movie in filtered_titles:
    print(movie)

#  Задача 2.2
print("\nСписок названий фильмов:")
print(filtered_titles)

#  Задача 2.3
print("\nФильтрованный словарь:")
print(filtered_dict)

#  Задача 2.4
print("\nСписок словарей:")
print(filtered_list_of_dicts)