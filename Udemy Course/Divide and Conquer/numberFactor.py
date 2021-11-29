def numberFactor(num):
    if num in [0, 1, 2]:
        return 1
    elif num == 3:
        return 2
    else:
        p1 = numberFactor(num - 1)
        p2 = numberFactor(num - 3)
        p3 = numberFactor(num - 4)
        return p1 + p2 + p3


print(numberFactor(5))
