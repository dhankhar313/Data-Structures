# TC: O(n^2)
def naive_solution(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if i + j == k:
                return True
    return False


def efficient_solution(arr, k):
    arr.sort()
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == k:
            return True
        elif arr[start] + arr[end] > k:
            end -= 1
        else:
            start += 1
    return False


def most_efficient_sol(arr, k):
    visited = {}
    for i in arr:
        if visited.get(k - i):
            return True
        else:
            visited[i] = True
    return False


if __name__ == '__main__':
    arr = [10, 50, 90, 12, -5, 432]
    naive_solution()
