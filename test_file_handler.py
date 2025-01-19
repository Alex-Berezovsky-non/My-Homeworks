import os
from file_hadler import FileHandler
def test_file_handler():
    handler = FileHandler()
    test_file = "test_file.txt"
    # Тест записи в файл
    handler.write_file(test_file,"Hello, World!\n")
    assert handler.read_file(test_file) == "Hello, World!\n"

    # Тест добавления в файл
    handler.append_file(test_file, "This is a test.\n")
    assert handler.read_file(test_file) == "Hello, World!\nThis is a test.\n"

    # Тест чтения несуществующего файла
    assert handler.read_file("non_existent_file.txt") == ""

    # Тест перезаписи файла 
    handler.write_file(test_file, "New content.\n")
    assert handler.read_file(test_file) == "New content.\n"

    # Удаление тестового файла 
    os.remove(test_file)
    print("Все тесты прошли успешно!")

if __name__ == "__main__":
    test_file_handler()