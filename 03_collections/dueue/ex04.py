from collections import deque


def choose_winner(arr: list[int]) -> str:
    dq = deque(arr)
    first_sum = 0
    second_sum = 0
    for i in range(len(dq)):
        if dq:
            first_sum += dq.popleft()
        if dq:
            second_sum += dq.pop()

    if first_sum == second_sum:
        return 'DRAW'
    return 'FIRST' if first_sum > second_sum else 'SECOND'


print(choose_winner(list(map(int, input().split()))))
