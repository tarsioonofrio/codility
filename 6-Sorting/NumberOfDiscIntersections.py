import random


def solution(a):
    d = {}
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
    a = []
    a[0] = 1
    a[1] = 5
    a[2] = 2
    a[3] = 1
    a[4] = 4
    a[5] = 0
    t = solution(a)
    print(a)
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
