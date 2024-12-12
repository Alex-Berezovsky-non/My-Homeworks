from City import cities_list

cities_set = set()

for city_dict in cities_list:
    cities_set.add(city_dict["name"])

bad_letters = {"Ь", "Ы", "Й"}
cities_set = {city for city in cities_set if city[-1] not in bad_letters}

last_city = None
while True:
    if last_city:
        last_letter = last_city[-1].upper() if last_city else ""
        print(f"Ваш ход. Назовите город на букву '{last_letter}'.")
    else:
        print("Ваш ход. Назовите любой город.")

    user_city = input().strip().title()

    if user_city.lower() == "стоп":
        print("Вы проиграли!")
        break

    if last_city and not (
        user_city in cities_set and user_city.startswith(last_letter)
    ):
        print("Неверный город! Вы проиграли.")
        break

    cities_set.remove(user_city)
    last_city = user_city

    computer_city = None
    for city in cities_set:
        if city.startswith(last_city[-1].upper()):
            computer_city = city
            break

    if not computer_city:
        last_letter = last_city[-2].upper() if len(last_city) > 1 else ""
        for city in cities_set:
            if city.startswith(last_letter):
                computer_city = city
                break

    if not computer_city:
        print("Компьютер не нашел город. Вы победили!")
        break

    print(f"Компьютер называет город: {computer_city}")
    cities_set.remove(computer_city)
    last_city = computer_city


from City import cities_list

# Создаем пустой сет для городов
cities_set = set()

# Наполняем сет названиями городов
for city_dict in cities_list:
    cities_set.add(city_dict["name"])

# Удаляем города, которые заканчиваются на "плохие буквы"
bad_letters = {"Ь", "Ы", "Й"}
cities_set = {city for city in cities_set if city[-1] not in bad_letters}

# Основной цикл игры
last_city = None
while True:
    if last_city:
        last_letter = (
            last_city[last_city.rfind(last_city[-1])].upper() if last_city else ""
        )
        print(f"Ваш ход. Назовите город на букву '{last_letter}'.")
    else:
        print("Ваш ход. Назовите любой город.")

    user_city = input().strip().title()

    if user_city.lower() == "стоп":
        print("Вы проиграли!")
        break

    if last_city and not (
        user_city in cities_set and user_city.startswith(last_letter)
    ):
        print("Неверный город! Вы проиграли.")
        break

    cities_set.remove(user_city)
    last_city = user_city

    # Ход компьютера
    computer_city = None
    for city in cities_set:
        if city.startswith(last_city[last_city.rfind(last_city[-1])].upper()):
            computer_city = city
            break

    # Если нет города на последнюю букву, пробуем предпоследнюю букву
    if not computer_city:
        last_letter = (
            last_city[last_city.rfind(last_city[-2])].upper()
            if len(last_city) > 1
            else ""
        )
        for city in cities_set:
            if city.startswith(last_letter):
                computer_city = city
                break

    if not computer_city:
        print("Компьютер не нашел город. Вы победили!")
        break

    print(f"Компьютер называет город: {computer_city}")
    cities_set.remove(computer_city)
    last_city = computer_city
