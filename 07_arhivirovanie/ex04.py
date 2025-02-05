from zipfile import ZipFile

with ZipFile('secrets.zip', mode='a') as arch:
    arch.write('SecretAgentManual.txt')
    arch.write('ChocolateCake_Recipe.pdf')
    arch.write('PirateTreasureMap.jpg')