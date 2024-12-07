from datetime import time

# Создаём множество для хранения уникальных времён
times = set()

# Перебираем часы, минуты и секунды
for hour in range(24):  # Часы от 0 до 23
    for minute in range(60):  # Минуты от 0 до 59
        for second in range(0, 60, 15):  # Секунды от 0 до 59 с шагом 15
            times.add(time(hour, minute, second))