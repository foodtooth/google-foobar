"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence
like all good rabbits do, the zombit population changes according to this bizarre formula, where R(n) is the number of
zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by
playing a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion
objected that this was too easy, and proposed a slightly different game: when is the last time that the zombit
population will be equal to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n
such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return
"None". S will be a positive integer no greater than 10^25.

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"

value >= index
"""

import argparse

cache = {0: 1, 1: 1, 2: 2}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    args = parser.parse_args()
    a = args.a
    print(answer(a))


def is_odd(n):
    return n & 1


def R(n):
    if n not in cache:
        if is_odd(n):
            n_temp = (n - 1) / 2
            cache[n] = R(n_temp - 1) + R(n_temp) + 1
        else:
            n_temp = n / 2
            cache[n] = R(n_temp) + R(n_temp + 1) + n_temp
    return cache[n]


def binary_search(start, end, v, part):
    while start < end:
        mid = (start + end) // 2
        mid += 1 if part == is_odd(mid) else 0
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
    r1 = binary_search(0, r, r, 0)
    r2 = binary_search(0, r, r, 1)
    result = r1 if r1 > r2 else r2
    return result if result != -1 else None


if __name__ == "__main__":
    main()
