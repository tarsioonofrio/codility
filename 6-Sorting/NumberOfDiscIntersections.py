import random
from collections import defaultdict


def solution(arr):
    m = [1, -1]
    # d = {e-i*n: [e] for e, i in enumerate(a) for n in m}
    d = defaultdict(lambda: defaultdict(lambda: []))
    value, index = -1, -1
    for e, a in enumerate(arr):
        k0 = e - a
        k1 = e + a
        d[k0][0].append(e)
        d[k1][1].append(e)
        if a > value:
            value = a
            index = e



def binary_search_recursive(d, max_value, max_index, count=0):
    # Check base case
    if len(d) > 0:
        din = defaultdict(lambda: set())
        setin = set()
        dout = defaultdict(lambda: set())
        max_value_in, max_index_in = -1, -1
        max_value_out, max_index_out = -1, -1
        for v, i in d.items():
            if max_index in i:
                continue
            if max_index - max_value <= v <= max_index + max_value:
                din[v] = i
                setin.update(i)
                for ii in i:
                    vv = abs(ii - v)
                    if vv > max_value_in:
                        max_value_in = vv
                        max_index_in = ii
            else:
                if i.issubset(setin) is False:
                    dout[v] = i
                    for ii in i:
                        vv = abs(ii - v)
                        if vv > max_value_out:
                            max_value_out = vv
                            max_index_out = ii

        # If element is present at the middle itself
        print(len(setin))
        if len(din) + len(dout) == 0:
            return len(setin)

        else:
            cin = binary_search_recursive(din, max_value_in, max_index_in, len(setin))
            cout = binary_search_recursive(dout, max_value_out, max_index_out, 0)
            return cin + cout

    else:
        # Element is not present in the array
        return count


def solution(arr):
    d = defaultdict(lambda: set())
    max_value, max_index = -1, -1
    for i, v in enumerate(arr):
        k0 = i - v
        k1 = i + v
        d[k0].add(i)
        d[k1].add(i)
        if v > max_value:
            max_value = v
            max_index = i
    c = binary_search_recursive(d, max_value, max_index, 0)
    return c


def test_correctness(f, a, n):
    list_a = [random.randint(0, a) for i in range(random.randint(0, n))]
    s = solution(list_a)
    return list_a, s


def test_performance(f, a, n):
    list_a = [random.randint(0, a) for i in range(random.randint(0, n))]
    s = solution(list_a)
    return s


def main():
    arr = [0] * 6
    arr[0] = 1
    arr[1] = 5
    arr[2] = 2
    arr[3] = 1
    arr[4] = 4
    arr[5] = 0
    t = solution(arr)
    print(arr)
    print("%d\t%d\t%s" % (t, 11, t == 11))

def test():
    ca = [0, 20]
    cn = [0, 20]
    for r in range(10):
        a, t = test_correctness(solution, ca, cn)
        print(a)
        print("%d" % t)

    pa = [0, 100000]
    pn = [0, .2147483647]
    """
    for r in range(10):
        t = test_performance(solution, pa, pb, pk)
        print("%d" % t)
    """


if __name__ == "__main__":
    main()
