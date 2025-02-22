from collections import UserString

# Напишите определение класса StringWithSort
class StringWithSort(UserString):
    def sort(self, *, key=None, reverse=False):
        return ''.join(sorted(list(self.data), key=key, reverse=reverse))

# Проверки для класса StringWithSort

# Пример использования:
s = StringWithSort("Golden retriver")
assert s.sort() == ' Gdeeeilnorrrtv'
assert s.data == 'Golden retriver'

assert s.sort(reverse=True) == 'vtrrronlieeedG '

new_s = StringWithSort('HelloMyFriend')
# При обычной сортироки сперва идут заглавные буквы потом строчные
assert new_s.sort() == 'FHMdeeillnory'
# Сортировка с ключом lower, который во время сравнения все буквы делает строчными
assert new_s.sort(key=str.lower) == 'deeFHillMnory'
print('Good')