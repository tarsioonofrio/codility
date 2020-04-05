import random
from collections import defaultdict
from math import inf

def solution(arr):

    def binary_search_recursive(d, best_value, best_index, min_value, max_value, count=0):
        # Check base case
        if len(d) > 0:
            din = defaultdict(lambda: set())
            setin = set()
            setout = set()
            dout = defaultdict(lambda: set())
            best_value_in, best_index_in = -1, -1
            best_value_out, best_index_out = -1, -1
            min_value_in, max_value_in = inf, -1
            min_value_out, max_value_out = inf, -1
            for v, i in d.items():
                if min_value <= v <= max_value:
                    din[v] = i
                    if v < min_value_in:
                        min_value_in = v
                    if v > max_value_in:
                        max_value_in = v

                    if best_index in i:
                        continue
                    setin.update(i)

                    if best_index - best_value <= v <= best_index + best_value:
                        for ii in i:
                            vv = abs(ii - v)
                            if vv > best_value_in and best_index != ii:
                                best_value_in = vv
                                best_index_in = ii

                else:
                    for ii in i:
                        vv = abs(ii - v)
                        if min_value <= ii + vv <= max_value:
                            continue
                        if min_value <= ii - vv <= max_value:
                            continue
                        if v < min_value_out:
                            min_value_out = v
                        if v > max_value_out:
                            max_value_out = v
                        dout[v].add(ii)
                        setout.update(i)
                        if vv > best_value_out:
                            best_value_out = vv
                            best_index_out = ii

            new_count = len(setin)

            if len(setin) + len(dout) == 0:
                return 0

            else:
                cin = binary_search_recursive(din, best_value_in, best_index_in, min_value_in, max_value_in, new_count)
                cout = binary_search_recursive(dout, best_value_out, best_index_out, min_value_out, max_value_out, new_count)
                print("*", best_index)
                print(new_count)
                print(din)
                print(dout)
                return cin + cout

        else:
            return count

    d = defaultdict(lambda: set())
    best_value, best_index = -1, -1
    min_value, max_value = inf, -1
    for i, v in enumerate(arr):
        k0 = i - v
        k1 = i + v
        d[k0].add(i)
        d[k1].add(i)
        if v > best_value:
            best_value = v
            best_index = i
        if k0 < min_value:
            min_value = k0
        if k1 > max_value:
            max_value = k1


    c = binary_search_recursive(d, best_value, best_index, min_value, max_value, 0)
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
    arr[1] = 4
    arr[2] = 2
    arr[3] = 1
    arr[4] = 4
    arr[5] = 0
    t = solution(arr)
    print(arr)
    print("%d\t%d\t%s" % (t, 12, t == 12))


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
