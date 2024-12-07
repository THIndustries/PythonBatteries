from collections import defaultdict


def get_inventory() -> set:
    return {'меч', 'лук', 'щит', 'зелье'}

heroes_dict = defaultdict(get_inventory)
heroes_list = ['Артур', 'Борис', 'Виктор']


for round in range(int(input())):
    curr_hero, curr_item = input().split()
    if curr_hero in heroes_list:
        heroes_list.remove(curr_hero)
    if curr_item in heroes_dict[curr_hero]:
        heroes_dict[curr_hero].remove(curr_item)
    else:
        del heroes_dict[curr_hero]


for hero in heroes_list:
    if hero not in heroes_dict:
        heroes_dict[hero] = get_inventory()


for hero, item in sorted(heroes_dict.items()):
    if len(heroes_dict[hero]) == 0:
        continue
    print(f'{hero}: {", ".join(sorted(item))}')