# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque


def solution(A, K):
    d = deque(A)
    d.rotate(K)
    return list(d)
