import re
from collections import Counter

text = input().lower()
new_text = re.sub(r'[., ]', '', text)

for k, v in Counter(new_text).items():
    print(k, v)
