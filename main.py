from functools import reduce

def process_numbers(numbers):
    numbers = list(filter(lambda x: x >=0 and x % 2 == 0, numbers))
    numbers = list(map(lambda x: x * x, numbers))
    try:
        numbers = reduce(lambda x, y: x + y, numbers)
    except TypeError:
        numbers = 0
    return numbers
