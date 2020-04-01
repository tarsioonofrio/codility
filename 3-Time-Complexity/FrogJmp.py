# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import ceil
def solution(X, Y, D):
    s = ceil((Y-X)/D)
    return s

#s = solution(0,0,0)
#print(s)

s = solution(10, 85, 30)
print(s)


s = solution(1, 5, 2)
print(s)
