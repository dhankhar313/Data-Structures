def solution(arr):
    visited = {}
    for i in arr:
        if visited.get(i):
            return i
        else:
            visited[i] = True
    return False


print(solution([1, 3, 5, 2, 4, 3, 1, 7, 9, 7, 9, 4, 3, 5]))
