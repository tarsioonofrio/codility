from collections import deque


def solution(size, direction):
    if len(size) == 1:
        return 1
    size = deque(size)
    direction = deque(direction)
    i = 0
    while True:
        if i == len(size) - 1:
            break

        s = size[i], size[i+1]
        d = direction[i], direction[i+1]

        if d[0] > d[1]:
            if s[0] > s[1]:
                del size[i + 1]
                del direction[i + 1]
            else:
                del size[i]
                del direction[i]
                i -= 1
        else:
            i += 1

    return len(size)


size = [0] * 5
size[0] = 4
size[1] = 3
size[2] = 2
size[3] = 1
size[4] = 5

direction = [0] * 5
direction[0] = 0
direction[1] = 1
direction[2] = 0
direction[3] = 0
direction[4] = 0


s = solution(size, direction)
print(size)
print(direction)
print(s)


size = [0] * 5
size[0] = 5
size[1] = 1
size[2] = 2
size[3] = 3
size[4] = 4

direction = [0] * 5
direction[0] = 1
direction[1] = 1
direction[2] = 1
direction[3] = 0
direction[4] = 1


s = solution(size, direction)
print(size)
print(direction)
print(s)



size = [0] * 5
size[0] = 5
size[1] = 1
size[2] = 2
size[3] = 3
size[4] = 4

direction = [0] * 5
direction[0] = 1
direction[1] = 1
direction[2] = 1
direction[3] = 0
direction[4] = 0


s = solution(size, direction)
print(size)
print(direction)
print(s)