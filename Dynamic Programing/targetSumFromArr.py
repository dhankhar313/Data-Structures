def can_sum(target, values, memo={}):
    if target in memo.keys():
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for i in values:
        rem = target - i
        if can_sum(rem, values, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_sum(7, [5, 4, 3, 7]))
    print(can_sum(300, [7, 14]))
