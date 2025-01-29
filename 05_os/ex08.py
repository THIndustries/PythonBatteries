DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
}

def alphabet():
    for k, v in DICTIONARY.items():
        yield k, v


for letter, word in alphabet():
    print(letter, word)