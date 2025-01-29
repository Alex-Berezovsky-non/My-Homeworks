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