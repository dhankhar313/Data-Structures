def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n - 1)
        # print(power)
        return power * 2


print(power_of_two(5))
