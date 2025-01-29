def find_level_element(value, lst, level=1):
    for element in lst:
        if isinstance(element, list):
            # Если элемент - это список, рекурсивно вызываем функцию для этого подсписка
            result = find_level_element(value, element, level + 1)
            if result != -1:
                return result
        elif element == value:
            return level
    return -1


print(find_level_element(5, [1, 2, 3, 4, 5, [5]]))
print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))
print(find_level_element(9, [1, 2, 3, 4, 5,
                             [6, 7, 8,
                              [[[9]], 1, [2, [3], 4], 5, 6]]]))