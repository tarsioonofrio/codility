# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    list_x = [0] * (max(A))
    x = 0
    s = -1
    for_break = False
    for t, a in enumerate(A):
        list_x[a - 1] = 1
        while list_x[x] == 1:
            x += 1

            if X == x:
                s = t
                for_break = True
                break

            if x + 1 > len(list_x):
                for_break = True
                break

        if for_break:
            break
    return s



t = (2, [1, 1, 1, 1])
t =  (5, [1, 3, 1, 4, 2, 3, 5, 4])

s = solution(*t)
print(s)
