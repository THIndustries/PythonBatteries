DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
}

def alphabet():
    while True:
        current_key = yield
        yield DICTIONARY[current_key]



coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.send('c'))



