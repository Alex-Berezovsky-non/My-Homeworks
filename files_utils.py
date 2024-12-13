import json
import csv
import yaml
def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    """
    Читает данные из JSON-файла.

    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию "utf-8").
    :return: Данные, считанные из файла.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)