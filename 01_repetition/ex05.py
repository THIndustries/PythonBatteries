from bookworms import bookworms
import json

boosk_list = set(input() for i in range(int(input())))


def check_worms(books: set[str]) -> None:
    for person in json.loads(bookworms):
        temp = [book for book in person['books_read'] if book in books]
        if len(temp) == len(books):
            print(person['name'])


check_worms(boosk_list)



'''
books = set(input() for _ in range(int(input())))

for reader in json.loads(bookworms):
    if books.issubset(reader['books_read']):
        print(reader['name'])
'''