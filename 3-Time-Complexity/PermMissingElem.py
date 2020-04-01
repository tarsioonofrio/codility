# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import zip_longest


def solution(A):
    if not A:
        return 1

    A.sort()
    size = max(2 + 1, len(A) + 1)

    s = 0
    for a, r in zip_longest(A, range(1, size)):
        if a != r:
            s = r
            break

    if s == 0:
        s = r + 1

    return s


A = [2, 3, 1, 5]
A = [2, 3]

s = solution(A)
print(s)
