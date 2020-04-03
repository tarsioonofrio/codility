from functools import reduce

def solution(a, b, k):
    return len(list(filter(lambda x: (x % k) == 0, range(a, b + 1))))


def solution(a, b, k):
    return reduce(lambda s, x: s + 1 if (x % k) == 0 else s, list(range(a, b + 1)), 0)


def solution(a, b, k):
    s = 0
    for x in range(a, b + 1):
        if (x % k) == 0:
            s += 1
    return s




a = 6
b = 11
k = 2

