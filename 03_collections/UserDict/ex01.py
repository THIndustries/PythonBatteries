from collections import UserDict
# Напишите определение класса ArchiveDict
class ArchiveDict(UserDict):

    def __delitem__(self, key):
        raise RuntimeError("Deletion not allowed")

    def popitem(self, key):
        raise RuntimeError("Deletion not allowed")



archive = ArchiveDict(
    {1: 'Дело № 1 о загадочном исчезновении обуви под кодовым названием «Пропала Пара»',
     4: 'Дело № 4: под юбкой правосудия: Расследование «Тайна Кружев»',
     10: 'Дело № 10: преступление на вечеринке: мотив «Скользкая Политика»'}
)


try:
    archive.pop(1)  # Дела нельзя удалять из архива
except RuntimeError:
    pass

try:
    archive.popitem(1)  # Дела нельзя удалять из архива
except RuntimeError:
    pass

try:
    del archive[10]  # Дела нельзя удалять из архива
except RuntimeError:
    pass

assert len(archive) == 3
archive[60] = 'Дело № 60: инцидент на трассе 60'
assert len(archive) == 4

print('Good')