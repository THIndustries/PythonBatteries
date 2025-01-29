from decimal import Decimal

curs, count = Decimal(input()), Decimal(input())

def show_money(curs, count):
    return curs * count

print(show_money(curs, count))