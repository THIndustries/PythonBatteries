from collections import defaultdict

magic = 'abracadabraabracadabraabracadabra'
statistics = defaultdict(list)

for i in range(len(magic)):
    statistics[magic[i]].append(i)

print(statistics)


