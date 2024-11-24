name_input = input("Введите ваше имя: ")
grade_input = input("Введите вашу оценку: ")
entry_level = "Начальный уровень"
intermediate_level = "Средний уровень"
sufficient_level = "Достаточный уровень"
high_level = "Высокий уровень"
if grade_input.isdigit():
    grade = int(grade_input)
    if 0 < grade < 4:
        level = entry_level
    elif 4 <= grade < 7:
        level = intermediate_level
    elif 7 <= grade < 10:
        level = sufficient_level
    elif 10 <= grade <= 13:
        level = high_level
    else:
        level = "Некорректная оценка"
else:
    level = "Некорректная оценка"

print(f"{name_input}, ваш уровень знаний: {level}")
