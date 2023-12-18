from collections import deque
from multiprocessing import Pool, cpu_count
from math import sqrt


def factorize(number):
    factors, second_half = [], deque()
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            second_half.appendleft(number // i)
    factors.extend(second_half)
    return factors


def parallel_factorize(num):
    pool = Pool(processes=cpu_count())
    res = pool.map(factorize, num)
    pool.close()
    pool.join()
    return res


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    results = parallel_factorize(numbers)

    a, b, c, d = results

    print('Test 1 ... ', end='')
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    print('passed')

    print('Test 2 ... ', end='')
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    print('passed')

    print('Test 3 ... ', end='')
    assert c == [1, 3, 9, 41, 123, 271, 369,
                 813, 2439, 11111, 33333, 99999]
    print('passed')

    print('Test 4 ... ', end='')
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70,
                 140, 76079, 152158, 304316, 380395,
                 532553, 760790, 1065106, 1521580,
                 2130212, 2662765, 5325530, 10651060]
    print('passed')
