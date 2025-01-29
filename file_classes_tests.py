from file_classes import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":
    # Тестирование JsonFile
    json_file = JsonFile('data.json')
    json_file.write({"name": "John", "age": 30})
    print("JSON Read after write:", json_file.read())
    json_file.append({"city": "New York"})
    print("JSON Read after append:", json_file.read())

    # Тестирование TxtFile
    txt_file = TxtFile('data.txt')
    txt_file.write("Hello, World!")
    print("TXT Read after write:", txt_file.read())
    txt_file.append("\nThis is a new line.")
    print("TXT Read after append:", txt_file.read())

    # Тестирование CsvFile
    csv_file = CsvFile('data.csv')
    csv_file.write([["Name", "Age"], ["John", "30"]])
    print("CSV Read after write:", csv_file.read())
    csv_file.append([["Jane", "25"]])
    print("CSV Read after append:", csv_file.read())