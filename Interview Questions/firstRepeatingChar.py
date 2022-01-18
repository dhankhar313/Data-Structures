def solution(string):
    visited = {}
    for i in string:
        if visited.get(i):
            return i
        else:
            visited[i] = True
    return None


print(solution('abcdebjuc'))
