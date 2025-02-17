# Словарь, сопоставляющий цифры и буквы шестнадцатеричной системы с их "выраженной" формой
digit_map = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',
    'a': 'A', 'A': 'A', 'b': 'B', 'B': 'B', 'c': 'C',
    'C': 'C', 'd': 'D', 'D': 'D', 'e': 'E', 'E': 'E',
    'f': 'F', 'F': 'F'
}


# Функция для преобразования строки в "выраженную" форму
def convert_to_spelled_out(lexeme):
    return ' '.join([digit_map[c] for c in lexeme])  # Объединяем символы в строку, разделяя пробелами

# Функция для проверки, является ли строка шестнадцатеричной
def is_hex(s):
    hex_chars = set('0123456789abcdefABCDEF')  # Множество допустимых символов
    return all(c in hex_chars for c in s)  # Проверяем, что все символы находятся в множестве

# Функция для проверки, является ли лексема корректной
def is_valid_lexeme(lexeme):
    # Проверяем, что лексема является шестнадцатеричной
    if not is_hex(lexeme):
        return False
    length = len(lexeme)
    # Проверяем, что длина лексемы не меньше 2
    if length < 2:
        return False
    second_char = lexeme[1].upper()  # Второй символ в верхнем регистре
    # Проверяем, является ли второй символ цифрой
    if second_char.isdigit():
        second_digit_val = int(second_char)  # Присваиваем значение цифры
    else:
        second_digit_val = 10 + (ord(second_char) - ord('A'))  # Преобразуем буквы от 'A' до 'F' в значения от 10 до 15
    # Проверяем условие длины лексемы
    if length <= second_digit_val:
        return False
    try:
        num = int(lexeme, 16)  # Преобразуем лексему в число
    except:
        return False  # Если произошла ошибка при преобразовании, возвращаем False
    # Проверяем дополнительные условия: число должно быть меньше 2048 и чётным
    if num > 2047 or num % 2 != 0:
        return False
    return True  # Если все проверки пройдены, возвращаем True

valid_numbers = []  # Список для хранения валидных чисел
buffer = ''  # Буфер для считывания данных

# Открываем файл для чтения
with open('input.txt', 'r') as file:
    while True:
        chunk = file.read(1024)  # Считываем данные порциями по 1024 байта
        if not chunk:  # Если данные закончились
            if buffer:  # Проверяем оставшийся буфер
                if is_valid_lexeme(buffer):  # Если буфер валиден
                    valid_numbers.append(buffer)  # Добавляем в список валидных чисел
            break  # Выходим из цикла
        buffer += chunk  # Добавляем прочитанный кусок к буферу
        parts = buffer.split(' ')  # Разбиваем буфер на части по пробелам
        # Проверяем, заканчивается ли буфер пробелом
        if buffer.endswith(' '):
            buffer = ''  # Если да, очищаем буфер
            parts = parts[:-1] if len(parts) > 0 else []  # Убираем последний элемент
        else:
            buffer = parts[-1] if parts else ''  # Если нет, сохраняем последний элемент в буфер
            parts = parts[:-1]  # Убираем последний элемент из частей
        # Проверяем валидные лексемы в части
        for part in parts:
            if part and is_valid_lexeme(part):  # Если часть не пустая и валидная
                valid_numbers.append(part)  # Добавляем в список валидных чисел

# Проверяем, были ли найдены валидные числа
if valid_numbers:
    print("Valid numbers:")
    for num in valid_numbers:  # Перебираем все валидные числа
        print(num)
    print(f"Total count: {len(valid_numbers)}")  # Выводим общее количество валидных чисел
    max_val = max(int(lex, 16) for lex in valid_numbers)  # Находим максимальное валидное число
    max_lexemes = [lex for lex in valid_numbers if int(lex, 16) == max_val]  # Извлекаем все лексемы с максимальным значением
    max_lexeme = max_lexemes[0]  # Берем первую лексему с максимальным значением
    spelled = convert_to_spelled_out(max_lexeme)  # Преобразуем её в "выраженную" форму
    print(f"Maximum number spelled out: {spelled}")  # Выводим максимальное число в "выраженной" форме
else:
    print("No valid numbers found.")
