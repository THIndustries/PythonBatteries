from datetime import date

# Инициализируем счетчик
count = 0

# Перебираем каждый год и месяц в заданном диапазоне
for year in range(2014, 2023):  # 2023 не включается
    for month in range(1, 13):  # Месяцы от 1 до 12
        if date(year, month, 1).weekday() == 0:  # 0 - понедельник
            count += 1

print(f"Общее число понедельников, которые были 1-м числом месяца с 2014 по 2022 год: {count}")