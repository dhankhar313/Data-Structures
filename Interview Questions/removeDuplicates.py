def solution(arr):
    visited = {}
    res = []
    for i in arr:
        if not visited.get(i):
            res.append(i)
            visited[i] = True
    return res


print(solution([1, 3, 5, 2, 4, 3, 1, 7, 9, 7, 9, 4, 3, 5]))
