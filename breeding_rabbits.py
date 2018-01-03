"""
R(0) = 0
R(1) = 1
R(n) = R(n - 1) + R(n - 2) (for n >= 2)

value >= index
"""

import argparse

cache = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    args = parser.parse_args()
    a = args.a
    answer(a)


def R(n):
    if n not in cache:
        cache[n] = R(n - 1) + R(n - 2)
    return cache[n]


def binary_search(start, end, v):
    if end < 4:
        end = 4

    while start <= end:
        mid = (start + end) // 2
        v_temp = R(mid)
        if v_temp == v:
            return mid
        elif v_temp > v:
            end = mid - 1
        elif v_temp < v:
            start = mid + 1
    return -1


def answer(str_S):
    r = int(str_S, 10)
    print(binary_search(0, r, r))


if __name__ == "__main__":
    main()
