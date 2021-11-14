def constant1(n):
    temp = 100 * 1000
    return temp


def constant2(n):
    temp = 100 * 1000
    temp1 = 1000 * 100000
    return temp, temp1


def linear1(n):
    for i in range(n):
        print(100 * 1000, end='')


def linear2(n):
    for i in range(n):
        print(100 * 1000)
        print(n)
    temp = 100 * 1000
    return temp


def exponential(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


def cubic(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


def logarithmic1(n):
    if n == 1:
        return 'Done'
    n = n // 2
    return logarithmic1(n)


def logarithmic2(n):
    while n > 1:
        n //= 2


def loglinear_nlogn(n):
    temp = n
    while n > 1:
        n //= 2  # logarithmic time
        for i in range(temp):  # linear time
            print(i)
