def naive_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return naive_traveller(m, n - 1) + naive_traveller(m - 1, n)


def dp_traveller(m, n, memo={}):
    if (m, n) in memo.keys():
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = dp_traveller(m, n - 1) + dp_traveller(m - 1, n)
    return memo[(m, n)]


if __name__ == "__main__":
    print(naive_traveller(1, 1))
    print(naive_traveller(2, 3))
    print(dp_traveller(1, 1))
    print(dp_traveller(2, 3))
    print(dp_traveller(18, 18))
