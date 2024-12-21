import os
import yaml  
from files_utils import (
    read_json, write_json, append_json,
    read_csv, write_csv, append_csv,
    read_txt, write_txt, append_txt,
    read_yaml  
)
# Тестовые данные
test_json_data = {"name": "Alice", "age": 30}
test_csv_data = [{"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
test_txt_data = "Hello, World!"
test_yaml_data = {"app_name": "WeatherApp", "settings": {"theme": "dark", "language": "en"}}

# Тестирование JSON
write_json(test_json_data, "test.json")
read_json_data = read_json("test.json")
print("JSON:", read_json_data)

# Тестирование CSV
write_csv(test_csv_data, "test.csv")
read_csv_data = read_csv("test.csv")
print("CSV:", read_csv_data)

# Тестирование TXT
write_txt(test_txt_data, "test.txt")
read_txt_data = read_txt("test.txt")
print("TXT:", read_txt_data)

# Тестирование YAML
with open("test.yaml", 'w', encoding='utf-8') as file:
    file.write(yaml.dump(test_yaml_data, allow_unicode=True))
read_yaml_data = read_yaml("test.yaml")
print("YAML:", read_yaml_data)