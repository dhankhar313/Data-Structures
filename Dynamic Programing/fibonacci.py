# This function is very slow because of same recursive calls again and again
def naive_fib(n):
    if n <= 2:
        return 1
    return naive_fib(n - 1) + naive_fib(n - 2)


# This function is much faster because it stores the values instead of calculating them again and again
def dp_fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if 0 <= n <= 2:
        return 1
    memo[n] = dp_fib(n - 1, memo) + dp_fib(n - 2, memo)
    for i in memo.values():
        print(i)


# print(dp_fib(int(input())))

if __name__ == "__main__":
    print(naive_fib(7))
    res = dp_fib(5)
    # print(res.keys())
