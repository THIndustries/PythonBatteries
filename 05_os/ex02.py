def reversed_recursive(data):
    if isinstance(data, list):
        reversed_list = []
        for item in reversed(data):
            reversed_list.append(reversed_recursive(item))  # Рекурсивный вызов
        return reversed_list
    return data


print(reversed_recursive([[1, 2, 3], [4, [5, [6]]], 7]))