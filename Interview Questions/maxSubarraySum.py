from math import inf


def solution(arr):
    localSum = 0
    globalSum = -float(inf)
    for i in arr:
        localSum = max(localSum, localSum + i)
        globalSum = max(localSum, globalSum)
    return globalSum


if __name__ == '__main__':
    print(solution([2, 3, -4, 8, 5]))
