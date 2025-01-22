from collections import deque

def use_command(command_list):
    for command in command_list:
        if command[0] == 'A':
            my_dq.append(int(command[2])) if command[1] == 'R' else my_dq.appendleft(int(command[2]))
        elif command[0] == 'D':
            my_dq.pop() if command[1] == 'R' else my_dq.popleft()
        else:
            my_dq.rotate() if command[1] == 'R' else my_dq.rotate(-1)


current_nums_list = list(map(int, input().split()))
my_dq = deque(current_nums_list)
commands_list = [(input().split()) for i in range(int(input()))]

use_command(commands_list)

print(my_dq)