# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import takewhile


def solution(a):
    a = sorted(set(a))
    a = list(filter(lambda x: x > 0, a))

    f = lambda x: (x[0] - x[1]) == 0
    s = list(takewhile(f, zip(a, range(1, len(a) + 1))))
    if s:
        return s[-1][1] + 1
    else:
        return 1


a = [1, 5, 6, 4, 1, 2]
print(a, solution(a))
a = [1, 2, 3]
print(a, solution(a))
a = [1, 3, 6, 4, 1, 2]
print(a, solution(a))
a = [-1, -3, 1, 3]
print(a, solution(a))
a = [-1, -3]
print(a, solution(a))


