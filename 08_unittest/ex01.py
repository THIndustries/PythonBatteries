import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    # Проверки на простые числа
    assert is_prime(2) is True
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    # Проверки на непростые числа
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    # Проверки на отрицательные числа
    assert not is_prime(-2)
    assert not is_prime(-5)
    assert not is_prime(-8)
    assert not is_prime(-10)
    logger.log(logging.DEBUG, 'all is good')

    print(200*1.5)