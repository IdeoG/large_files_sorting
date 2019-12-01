import random

from utils import time_it


@time_it
def generate_file(size=1_000_000, filename='./data.txt'):
    MAX_VALUE = 2 ** 63
    with open(filename, 'w') as f:
        for _ in range(size):
            line = f'{random.randint(-MAX_VALUE, MAX_VALUE - 1)}\n'
            f.write(line)
