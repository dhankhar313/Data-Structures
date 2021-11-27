def power_of_n(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    return base * power_of_n(base, power - 1)


print(power_of_n(4, 4))
