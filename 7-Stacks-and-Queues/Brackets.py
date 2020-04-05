from collections import deque


def solution(string):
    if len(string) == 0:
        return 1
    d = {"{": 0, "[": 1, "(": 2, "}": 3, "]": 4, ")": 5}
    stack = deque()
    stack.append(string[0])
    for s in string[1:]:
        n = d[s]
        if len(stack) == 0:
            stack.append(s)
            continue
        last = d[stack[-1]]
        if n == last + 3:
            stack.pop()
        else:
            stack.append(s)
    s = len(stack) == 0
    return int(s)


string = "([)()]"
s = solution(string)
print(s, string)
string = "{[()()]}"
s = solution(string)
print(s, string)



