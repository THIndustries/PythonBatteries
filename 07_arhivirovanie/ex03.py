from zipfile import ZipFile

# Создаем ZIP-архив
with ZipFile("my_archive.zip", "w") as my_zip:
    # Записываем текстовую строку в архив с указанными именами "hello.txt" и "world.txt"
    my_zip.writestr("hello.txt", "Hello")
    my_zip.writestr("world.txt", "World")

    # Записываем байтовую строку в архив с указанным именем "hello_world.txt"
    binary_data = b"Hello world!"
    my_zip.writestr("hello_world.txt", binary_data)

print("ZIP-архив 'my_archive.zip' успешно создан.")