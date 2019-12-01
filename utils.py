import tempfile
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print(f'Time in func = {func.__name__} equals to {1000 * (e - s):0.2f} ms')
        return result

    return wrapper


@time_it
def get_sorted_bucket_iters(bucket_length, cached_ints_length, in_file):
    buckets = []
    while True:
        sorted_chunk = get_sorted_chunk_from_file(in_file, bucket_length)

        if not sorted_chunk:
            break

        t_file = tempfile.TemporaryFile()
        for data in sorted_chunk:
            t_file.write(f'{data}\n'.encode())

        t_file.seek(0)
        buckets.append(get_ints_from_file(t_file, cached_ints_length))

    return buckets


def get_sorted_chunk_from_file(file, chunk_length=40_000):
    chunk = []
    for i in range(chunk_length):
        line = file.readline().rstrip()
        if line:
            chunk.append(int(line))
    chunk = sorted(chunk)
    return chunk


def get_ints_from_file(file, chunk_length=1_000):
    while True:
        chunk = []
        for i in range(chunk_length):
            line = file.readline().rstrip()
            if line:
                chunk.append(line)

        if not chunk:
            return

        for x in chunk:
            yield int(x)
