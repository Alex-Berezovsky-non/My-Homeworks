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
def write_json(data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Записывает данные в JSON-файл.

    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию "utf-8").
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def append_json(data: list[dict], file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в существующий JSON-файл.

    :param data: Список словарей с данными для добавления.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию "utf-8").
    """
    existing_data = read_json(file_path, encoding) if file_path else []
    existing_data.extend(data)
    write_json(existing_data, file_path, encoding)
def read_csv(file_path: str, delimiter: str = ';', encoding: str = "windows-1251") -> list[dict]:
    """
    Читает данные из CSV-файла.

    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей в файле (по умолчанию ";").
    :param encoding: Кодировка файла (по умолчанию "windows-1251").
    :return: Данные, считанные из файла.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)