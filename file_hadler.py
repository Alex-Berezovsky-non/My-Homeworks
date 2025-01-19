class FileHandler:
    """
    Класс для работы с текстовыми файлами.
    Предоставляет методы для чтения, записи и добавления данных в TXT файлы.
    """

    @staticmethod
    def read_file(filepath: str) -> str:
        """
        Читает содержимое файла и возвращает его в виде строки.
        Если файл не найден, возвращает пустую строку.

        :param filepath: Путь к файлу.
        :return: Содержимое файла в виде строки.
        """
        try:
            with open(filepath,'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return""

    @staticmethod
    def write_file(filepath: str, *data: str) -> None:
        """
        Записывает переданные строки в файл.
        Если файл существует, он будет перезаписан.

        :param filepath: Путь к файлу.
        :param data: Строки для записи в файл.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Произошла ошибка при записи файла: {e}")
    @staticmethod
    def append_file(filepath: str, *data:str) -> None:
        """
        Добавляет переданные строки в конец файла.
        Если файл не существует, он будет создан.

        :param filepath: Путь к файлу.
        :param data: Строки для добавления в файл.
        """
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                file.writelines(data)
        except Exception as e:
            print(f"Произошла ошибка при добавлении данных в файл: {e}")