from collections import deque
import string
def is_palindrome(s: str) -> bool:
    table = str.maketrans("", "", string.punctuation)
    dq = deque(s.translate(table).lower().replace(' ', ''))

    return dq == deque(reversed(dq))



assert is_palindrome("A man, a plan, a canal, Panama") is True
assert is_palindrome("race car") is True
assert is_palindrome("hello") is False