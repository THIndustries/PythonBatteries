def get_file_data(filename: str) -> list[float]:
    with open(filename) as file:
       lines = file.readlines()
       return [float(line.strip()) for line in lines]


def calculate_sum(filename: str) -> float:
    """ return the sum of numbers in a text file """
    numbers = get_file_data(filename)
    return sum(numbers)