from datetime import date

def is_programmers_day(dt: date) -> bool:
    return dt.strftime('%j') == '256'

# Проверки
# Невисокосный год
assert is_programmers_day(date(2023, 9, 13))
assert not is_programmers_day(date(2023, 9, 12))
assert not is_programmers_day(date(2023, 12, 30))

# Високосный год
assert is_programmers_day(date(2024, 9, 12))
assert not is_programmers_day(date(2024, 9, 13))
assert not is_programmers_day(date(2024, 2, 22))

print('Good')