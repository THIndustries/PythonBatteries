def slugify(arg: str)-> str:
    temp = arg.lower().strip()
    new_temp = ''.join([char for char in temp if char not in "!@#$%^&*()_+={}[]|\:;'<>,.?/~`"])
    if '--' not in new_temp:
        return '-'.join(new_temp.split())
    else:
        result = []
        for i in range(len(new_temp)):
            if new_temp[i] != '-':
                result.append(new_temp[i])
            if new_temp[i] == '-' and new_temp[i-1] != '-':
                result.append(new_temp[i])
        return ''.join(result)



assert slugify("Hello World") == "hello-world"
assert slugify("Hello, World!") == "hello-world"
assert slugify("The 20th Century") == "the-20th-century"
assert slugify("    Hello      World     ") == "hello-world"
assert slugify("Hello World   ") == "hello-world"
assert slugify("") == ""
assert slugify("!@#$%^&*()_+={}[]|\:;'<>,.?/~`") == ""
assert slugify('hello----world') == 'hello-world'

print(slugify("What is My Name?"))