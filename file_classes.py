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
class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    Наследует абстрактный класс AbstractFile.
    """

    def __init__(self, file_path: str) -> None:
        """
        Инициализация объекта TxtFile.

        :param file_path: Путь к текстовому файлу.
        """
        self.file_path = file_path

    def read(self) -> str:
        """
        Чтение данных из текстового файла.

        :return: Данные в виде строки.
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, data: str) -> None:
        """
        Запись данных в текстовый файл.

        :param data: Данные для записи (строка).
        """
        with open(self.file_path, 'w') as file:
            file.write(data)

    def append(self, data: str) -> None:
        """
        Добавление данных в текстовый файл.

        :param data: Данные для добавления (строка).
        """
        with open(self.file_path, 'a') as file:
            file.write(data)


class CsvFile(AbstractFile):
    """
    Класс для работы с CSV-файлами.
    Наследует абстрактный класс AbstractFile.
    """

    def __init__(self, file_path: str) -> None:
        """
        Инициализация объекта CsvFile.

        :param file_path: Путь к CSV-файлу.
        """
        self.file_path = file_path

    def read(self) -> List[List[str]]:
        """
        Чтение данных из CSV-файла.

        :return: Данные в виде списка строк.
        """
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def write(self, data: List[List[str]]) -> None:
        """
        Запись данных в CSV-файл.

        :param data: Данные для записи (список строк).
        """
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data: List[List[str]]) -> None:
        """
        Добавление данных в CSV-файл.

        :param data: Данные для добавления (список строк).
        """
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)