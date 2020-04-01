# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter


def solution(A):
    s = [k for k, v in Counter(A).items() if v % 2 != 0]
    if s:
        return s[0]
    else:
        return 0

s = solution([9, 3, 9, 3, 9, 7, 7, 9])
print(s)