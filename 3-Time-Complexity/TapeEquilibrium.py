# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import itertools as it


def solution(A):
    forward = list(it.accumulate(A))
    forward = forward[:-1]
    backward = list(it.accumulate(A[::-1]))
    backward = backward[::-1]
    backward = backward[1:]
    diff = list(map(lambda x, y: abs(x - y), forward, backward))
    return min(diff)

