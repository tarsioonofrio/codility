from functools import reduce
from math import floor


def solution(a, b, k):
    return len(list(filter(lambda x: (x % k) == 0, range(a, b + 1))))


def solution(a, b, k):
    s = 0
    for x in range(a, b + 1):
        if (x % k) == 0:
            s += 1
    return s


def solution(a, b, k):
    m = a % k
    a1 = a - m
    if m != 0:
        a1 = a1 + k
    return reduce(lambda s, x: s + 1, range(a1, b + 1, k), 0)


def solution(a, b, k):
    if b == a:
        if b % k == 0:
            return 1
        else:
            return 0
    m = a % k
    a1 = a - m
    if m != 0:
        a1 = a1 + k
    return reduce(lambda s, x: s + 1, range(a1, b + 1, k), 0)


def solution(a, b, d):
    if b == a:
        if b % d == 0:
            return 1
        else:
            return 0
    n = (b - a) / d + 1
    return floor(n)


A = 11
B = 13
K = 2
print(solution(A, B, K))


A = 6
B = 11
K = 2
print(solution(A, B, K))


A = B = 0
K = 11
print(solution(A, B, K))

A = B = 1
K = 11
print(solution(A, B, K))

A = 101
B = 12345 * 10000
K = 10000
print(solution(A, B, K))


A = 100
B = 123 * 1000000
K = 10000
print(solution(A, B, K))


A = 100
B = 123 * 1000000
K = 2
print(solution(A, B, K))

A = 0
B = 2 * 1000000000
K = 10000
print(solution(A, B, K))


A = 0
B = 2 * 1000000000
K = 1
print(solution(A, B, K))


