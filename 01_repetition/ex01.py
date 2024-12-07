def print_figure(figure_type: str, height: int)-> None:
    tr = '#'
    if figure_type == 'sq' and 1 <= height <= 9:
        width: int = height * 2
        for i in range(height):
            for j in range(width):
                print('#', end='')
            print()
    elif figure_type == 'tr' and 1 <= height <= 9:
        for _ in range(height):
            print(f'{tr:^{height*2}}')
            tr += '##'
    else:
        print('WRONG_DATA')

fig = input()
size = int(input())

print_figure(fig, size)