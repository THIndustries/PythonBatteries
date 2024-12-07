from collections import Counter

my_list = []
while (word := input()) != 'End':
    my_list.append(word)

my_string = ' '.join(my_list)

for word, count in Counter(my_string.split()).items():
    print(f'{word}: {count}')