from datetime import datetime


def is_third_tuesday(dt_str: str) -> bool:
    # Преобразуем строку в объект даты
    date = datetime.strptime(dt_str, '%b %d, %Y')
    # Проверяем, является ли день вторником
    if date.weekday() != 1:  # 1 соответствует вторнику
        return False
    # Получаем номер дня в месяце
    day_of_month = date.day
    # Проверяем, является ли это третьим вторником
    return 15 <= day_of_month <= 21

assert is_third_tuesday("Sep 19, 2023")
assert not is_third_tuesday("Sep 12, 2023")
assert is_third_tuesday("Jul 18, 2023")
assert not is_third_tuesday("Jul 11, 2023")
assert not is_third_tuesday('Jun 23, 2015')
assert is_third_tuesday('Jun 16, 2015')
assert is_third_tuesday('Jul 21, 2015')
assert is_third_tuesday("Oct 20, 2015")
assert is_third_tuesday("Nov 17, 2015")


print('Good')