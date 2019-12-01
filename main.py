from data_generator import generate_file
from data_sorter import sort_large_file

if __name__ == '__main__':
    generate_file(100_000_000)
    sort_large_file(bucket_length=40_000, cached_ints_length=100)
