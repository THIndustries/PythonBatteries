def compress_string(string: str) -> str:
    if not string:
        return string
    string_second = string[:].lower()  # Преобразуем строку в нижний регистр
    result = []
    count = 1
    # Проходим по строке
    for i in range(1, len(string_second)):
        if string_second[i] == string_second[i - 1]:
            count += 1
        else:
            result.append(string_second[i - 1] + str(count))  # Добавляем символ и количество
            count = 1  # Сбрасываем счетчик для нового символа
    # Добавляем последний символ
    result.append(string_second[-1] + str(count))
    # Формируем сжатую строку
    compressed_string = ''.join(result)
    # Если сжатая строка не короче исходной, возвращаем исходную строку
    return compressed_string if len(compressed_string) < len(string) else string

# Тестовые случаи с корректными входными данными
assert compress_string("aaaabbbc") == "a4b3c1"
assert compress_string("abbbbbd") == "a1b5d1"
assert compress_string("wwwwwww") == "w7"
assert compress_string("") == ""


# Тестовые случаи с входными данными, которые не нуждаются в сжатии
assert compress_string("abcd") == "abcd"
assert compress_string("xyz") == "xyz"
assert compress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"

# Тестовые случаи с регистронезависимостью
assert compress_string("aaAAaa") == "a6"
assert compress_string("aAaAA") == "a5"
assert compress_string("AaBbCc") == "AaBbCc"
assert compress_string("aaaAbbCaa") == "a4b2c1a2"
assert compress_string("AAAABBBCC") == "a4b3c2"

# Тестовые случаи с длинной строки
assert compress_string("a" * 1000000) == "a1000000"
assert compress_string("a" * 1000000 + 'b' * 500) == "a1000000b500"
assert compress_string("abcdefghijk" + "w" * 10000) == "a1b1c1d1e1f1g1h1i1j1k1w10000"