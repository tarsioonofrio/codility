import random
from collections import defaultdict

def binary_search_interactive(arr, ln, r, x):
    while ln <= r:

        mid = ln + (r - ln) // 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            ln = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


def binary_search_recursive(arr, ln, r, x):
    # Check base case
    if r >= ln:

        mid = ln + (r - ln) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, ln, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

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

def solution(arr):
    d = defaultdict(lambda: set())
    value, index = -1, -1
    for k, v in enumerate(arr):
        k0 = k - v
        k1 = k + v
        d[k0].add(k)
        d[k1].add(k)
        if v > value:
            value = v
            index = k

    din = defaultdict(lambda: set())
    setin = set()
    dout = defaultdict(lambda: set())
    value1, index1 = -1, -1
    for k, v in d.items():
        if index in v:
            continue
        if index - value <= k <= index + value:
            din[k] = v
            setin.update(v)
            #for v1 in v:
            #    if v1 > value1:
            #        value1 = v1
            #        index1 = k
        else:
            dout[k] = v
            #print(v, index, value)
            #if v.issubset(setin) is False and k != index:


    return 0


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
