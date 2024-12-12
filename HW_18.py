input_str = input("Введите ваш текст на русском или английском языке: ")
input_int = int(input("Введите ваше число для сдвига: "))
result = ""
for char in input_str:
    if char.isalpha():
        if char.islower():
            base = ord("а") if ord(char) >= ord("а") else ord("a")
        else:
            base = ord("А") if ord(char) >= ord("А") else ord("A")

        if base == ord("а") or base == ord("А"):
            new_char_code = (ord(char) - base + input_int) % 33 + base
        else:
            new_char_code = (ord(char) - base + input_int) % 26 + base

        new_char = chr(new_char_code)
        result += new_char
    else:
        result += char
print("Результат:", result)
