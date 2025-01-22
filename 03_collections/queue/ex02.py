from collections import deque

def find_max_nums_for_windows(arr: list[int], win_size: int) -> list:
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Удаляем индексы, выходящие за пределы окна
        if dq and dq[0] < i - win_size + 1:
            dq.popleft()

        # Удаляем из дека все элементы меньше текущего числа
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Добавляем текущий индекс в дек
        dq.append(i)

        # Добавляем максимум в результат, когда окно становится валидным
        if i >= win_size - 1:
            result.append(nums[dq[0]])

    print(*(i for i in result))

nums, window_size = list(map(int, input().split())), int(input())

find_max_nums_for_windows(nums, window_size)