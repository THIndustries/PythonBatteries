from zipfile import ZipFile

with ZipFile('numbers.zip', mode='a') as arch:
    for num in range(10):
        arch.writestr(f'number_{num}.txt', f"This is number {num}")