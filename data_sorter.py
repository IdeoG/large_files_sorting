import heapq

from utils import time_it, get_sorted_bucket_iters


@time_it
def sort_large_file(in_filename='./data.txt', out_filename='./sorted_data.txt',
                    bucket_length=40_000, cached_ints_length=1_000):
    in_file = open(in_filename, 'r')
    bucket_iters = get_sorted_bucket_iters(bucket_length, cached_ints_length, in_file)

    xs = []
    out_file = open(out_filename, 'w')

    for x in heapq.merge(*bucket_iters):
        xs.append(x)
        if len(xs) > cached_ints_length:
            for data in xs:
                out_file.write(f'{data}\n')
            del xs[:]

    if xs:
        for data in xs:
            out_file.write(f'{data}\n')

    in_file.close()
    out_file.close()
