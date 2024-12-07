from datetime import date


day, month, year = (int(input()) for _ in range(3))

print(date(year, month, day))