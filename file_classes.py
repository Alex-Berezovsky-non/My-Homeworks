from abc import ABC, abstractmethod
import json
import csv
from typing import List, Dict, Any, Union
class AbstractFile(ABC):
    """
    Абстрактный класс для работы с файлами.
    Определяет интерфейс для чтения, записи и добавления данных.
    """

    @abstractmethod
    def read(self) -> Union[Dict, List, str]:
        """
        Абстрактный метод для чтения данных из файла.

        :return: Данные из файла (зависит от типа файла).
        """
        pass

    @abstractmethod
    def write(self, data: Union[Dict, List, str]) -> None:
        """
        Абстрактный метод для записи данных в файл.

        :param data: Данные для записи.
        """
        pass

    @abstractmethod
    def append(self, data: Union[Dict, List, str]) -> None:
        """
        Абстрактный метод для добавления данных в файл.

        :param data: Данные для добавления.
        """
        pass
class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    Наследует абстрактный класс AbstractFile.
    """

    def __init__(self, file_path: str) -> None:
        """
        Инициализация объекта JsonFile.

        :param file_path: Путь к JSON-файлу.
        """
        self.file_path = file_path

    def read(self) -> Dict[str, Any]:
        """
        Чтение данных из JSON-файла.

        :return: Данные в виде словаря.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data: Dict[str, Any]) -> None:
        """
        Запись данных в JSON-файл.

        :param data: Данные для записи (словарь).
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def append(self, data: Dict[str, Any]) -> None:
        """
        Добавление данных в JSON-файл.

        :param data: Данные для добавления (словарь).
        """
        existing_data = self.read()
        existing_data.update(data)
        self.write(existing_data)
