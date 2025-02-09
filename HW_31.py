from dataclasses import dataclass
import json
from collections import defaultdict
from typing import Optional, List, Union

# Класс для хранения информации о городе
@dataclass
class City:
    name: str  # Название города
    population: int  # Население города
    subject: str  # Субъект федерации
    district: str  # Федеральный округ
    latitude: str  # Широта
    longitude: str  # Долгота
    is_used: bool = False  # Флаг, указывающий, был ли город использован в игре

# Класс для работы с JSON-файлом
class JsonFile:
    def __init__(self, filename: str):
        self.filename = filename  # Имя файла

    # Метод для чтения данных из JSON-файла
    def read_data(self) -> list:
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    # Метод для записи данных в JSON-файл
    def write_data(self, data: list) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

# Класс для сериализации и десериализации данных о городах
class CitiesSerializer:
    def __init__(self, city_data: list):
        self.all_cities: List[City] = []  # Список всех городов
        for item in city_data:
            # Создание объекта City из данных JSON
            city = City(
                name=item['name'],
                population=item['population'],
                subject=item['subject'],
                district=item['district'],
                latitude=item['coords']['lat'],
                longitude=item['coords']['lon'],
                is_used=item.get('is_used', False)  # По умолчанию is_used = False
            )
            self.all_cities.append(city)

    # Метод для получения всех городов
    def get_all_cities(self) -> List[City]:
        return self.all_cities

    # Метод для сериализации городов в список словарей
    def serialize(self) -> list:
        return [{
            "name": city.name,
            "population": city.population,
            "subject": city.subject,
            "district": city.district,
            "coords": {"lat": city.latitude, "lon": city.longitude},
            "is_used": city.is_used
        } for city in self.all_cities]

# Класс для управления игрой
class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities_serializer = cities_serializer
        self.all_cities = cities_serializer.get_all_cities()  # Все города
        self.first_letter_map = defaultdict(list)  # Словарь для быстрого поиска городов по первой букве
        self.last_city: Optional[City] = None  # Последний названный город
        self.last_player: Optional[str] = None  # Последний игрок (человек или компьютер)
        self._update_first_letter_map()  # Инициализация словаря first_letter_map

    # Метод для обновления словаря first_letter_map
    def _update_first_letter_map(self) -> None:
        self.first_letter_map.clear()
        for city in self.all_cities:
            if not city.is_used:
                first_letter = city.name[0].lower()  # Первая буква названия города
                self.first_letter_map[first_letter].append(city)

    # Метод для начала игры
    def start_game(self) -> None:
        for city in self.all_cities:
            if not city.is_used:
                self._mark_city_as_used(city)  # Помечаем город как использованный
                self.last_city = city
                self.last_player = 'computer'
                print(f"Компьютер начинает с города: {city.name}")
                return
        raise ValueError("Нет доступных городов для начала игры")

    # Метод для пометки города как использованного
    def _mark_city_as_used(self, city: City) -> None:
        city.is_used = True
        first_letter = city.name[0].lower()
        if city in self.first_letter_map[first_letter]:
            self.first_letter_map[first_letter].remove(city)

    # Метод для хода человека
    def human_turn(self, city_input: str) -> None:
        city = next((c for c in self.all_cities if c.name.lower() == city_input.lower()), None)
        if not city:
            raise ValueError("Город не найден")
        if city.is_used:
            raise ValueError("Город уже использован")
        if self.last_city and city.name[0].lower() != self.last_city.name[-1].lower():
            raise ValueError("Неверная первая буква")
        self._mark_city_as_used(city)
        self.last_city = city
        self.last_player = 'human'

    # Метод для хода компьютера
    def computer_turn(self) -> Optional[City]:
        if not self.last_city:
            return None
        last_letter = self.last_city.name[-1].lower()  # Последняя буква последнего города
        possible_cities = self.first_letter_map.get(last_letter, [])  # Возможные города
        if not possible_cities:
            return None

        # Предпочтение городам, которые не ведут в тупик
        good_cities = [c for c in possible_cities if self.first_letter_map.get(c.name[-1].lower())]
        selected_city = good_cities[0] if good_cities else possible_cities[0]

        self._mark_city_as_used(selected_city)
        self.last_city = selected_city
        self.last_player = 'computer'
        return selected_city

    # Метод для проверки окончания игры
    def check_game_over(self) -> Optional[str]:
        if not self.last_city:
            return None
        last_letter = self.last_city.name[-1].lower()
        return self.last_player if not self.first_letter_map.get(last_letter) else None

    # Метод для сохранения состояния игры (заглушка)
    def save_game_state(self) -> None:
        pass

# Класс для управления игровым процессом
class GameManager:
    def __init__(self, json_file: JsonFile, cities_serializer: CitiesSerializer, city_game: CityGame):
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    # Метод для запуска игры
    def __call__(self) -> None:
        self.run_game()

    # Основной игровой цикл
    def run_game(self) -> None:
        self.city_game.start_game()  # Начинаем игру
        while True:
            try:
                human_city = input("Введите город: ")  # Ход человека
                self.city_game.human_turn(human_city)
            except ValueError as e:
                print(f"Ошибка: {e}. Вы проиграли.")
                break

            # Проверка на окончание игры после хода человека
            if winner := self.city_game.check_game_over():
                self.display_game_result(winner)
                break

            # Ход компьютера
            computer_city = self.city_game.computer_turn()
            if not computer_city:
                print("Компьютер не может найти город. Вы победили!")
                break
            print(f"Компьютер назвал город: {computer_city.name}")

            # Проверка на окончание игры после хода компьютера
            if winner := self.city_game.check_game_over():
                self.display_game_result(winner)
                break

    # Метод для отображения результата игры
    def display_game_result(self, winner: str) -> None:
        print("Поздравляем! Вы победили!" if winner == 'human' else "Компьютер победил. Попробуйте еще раз!")

# Точка входа в программу
if __name__ == "__main__":
    json_file = JsonFile("data.json")  # Загрузка данных из JSON-файла
    cities_serializer = CitiesSerializer(json_file.read_data())  # Сериализация данных
    city_game = CityGame(cities_serializer)  # Инициализация игры
    game_manager = GameManager(json_file, cities_serializer, city_game)  # Менеджер игры
    game_manager()  # Запуск игры