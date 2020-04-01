# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary = "{0:b}".format(N)
    list_binary = list(binary)
    list_gap = [e for e, b in enumerate(list_binary) if b == '1']
    max(list_gap)

    list_gap_norm = []
    for g0, g1 in zip(list_gap[:-1], list_gap[1:]):
        list_gap_norm.append(g1 - g0 - 1)

    if list_gap_norm:
        return max(list_gap_norm)
    else:
        return 0



print(solution(1041))