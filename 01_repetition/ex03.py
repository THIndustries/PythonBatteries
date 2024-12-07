from people_list import people
import json

my_dict = json.loads(people)
for person in sorted(my_dict, key=lambda x: (x['age'], x['name'])):
    print(f"{person['name']} {person['surname']}, {person['age']} years old")


