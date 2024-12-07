from collections import Counter


def find_difference_with_counter(lst1: list, lst2: list) -> list:
    counter1 = Counter(lst1)
    counter2 = Counter(lst2)

    # Вычитаем счетчики
    result_counter = counter1 - counter2

    # Преобразуем результат в список, повторяя элементы соответствующее количество раз
    result = list(result_counter.elements())

    return result

print(find_difference_with_counter([1, 1, 2, 3, 3, 4, 4, 5, 6, 7],
                                    [1, 1, 2, 4, 5, 6]))