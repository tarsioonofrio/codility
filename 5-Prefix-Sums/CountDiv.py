from functools import reduce
from math import floor, ceil
import random

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


def solution(a, b, k):
    if b == a:
        if b % k == 0:
            return 1
        else:
            return 0
    if k == 0:
        return 0
    if a > b:
        return -1
    a1 = ceil(a/k) * k
    b1 = floor(b/k) * k
    n = (b1 - a1) / k + 1
    return floor(n)


def test(f, a, b, k):
    ra = random.randint(a[0], a[1])
    rb = random.randint(ra, b[1])
    rk = random.randint(k[0], k[1])
    s = f(ra, rb, rk)
    return ra, rb, rk, s


def main():
    a = 6
    b = 11
    k = 2
    t = solution(a, b, k)
    print(a, b, k, t)
    print("%d\t%d\t%d\t%d\t%d\t%s" % (a, b, k, t, 3, t == 3))

    ca = [0, 20]
    cb = [0, 20]
    ck = [0, 20]
    for r in range(10):
        t = test(solution, ca, cb, ck)
        print("%d\t%d\t%d\t%d" % (t[0], t[1], t[2], t[3]))

    pa = [0, 2000000000]
    pb = [0, 2000000000]
    pk = [0, 2000000000]
    for r in range(10):
        t = test(solution, pa, pb, pk)
        print("%d\t%d\t%d\t%d" % (t[0], t[1], t[2], t[3]))


if __name__ == "__main__":
    main()


"""
A = 11
B = 13
K = 2
print(solution(A, B, K))
a = A
b = B
k = K

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
"""

