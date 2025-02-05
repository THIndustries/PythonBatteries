import re

def decompress_string(compressed: str) -> str:
    if not any(char.isdigit() for char in compressed):
        return compressed.lower()

    # Используем регулярное выражение для поиска пар "буква + число"
    pattern = re.compile(r'([a-zA-Z])(\d*)')
    result = []

    for char, count in pattern.findall(compressed):
        # Если нет числа после буквы, считаем его равным 1
        repeat = int(count) if count else 1
        result.append(char * repeat)

    return ''.join(result).lower()




# Тестовые случаи

print(decompress_string("a4b3c1"))
assert decompress_string("a4b3c1") == "aaaabbbc"
assert decompress_string("a1b5d1") == "abbbbbd"
assert decompress_string("w7") == "wwwwwww"
assert decompress_string("") == ""
assert decompress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
assert decompress_string("abcd") == "abcd"
assert decompress_string("xyz") == "xyz"

assert decompress_string("a6") == "aaaaaa"
assert decompress_string("a5") == "aaaaa"

assert decompress_string("AaBbCc") == "aabbcc"
assert decompress_string("a4b2c1a2") == "aaaabbcaa"
assert decompress_string("a4b3c2") == "aaaabbbcc"
assert decompress_string("a1000000") == "a" * 1000000
assert decompress_string("a1000000b500") == "a" * 1000000 + 'b' * 500
assert decompress_string("a1b1c1d1e1f1g1h1i1j1k1w10000") == "abcdefghijk" + "w" * 10000