def checkDuplicates(string):
    visited = {}
    for i in string:
        if visited.get(i):
            return True
        else:
            visited[i] = True
    return False


def solution(string):
    max_len = 0
    start = 0
    indexes = [-1] * 128
    for i in range(len(string)):
        print('i: ', i, ord(string[i]))
        print('Idx: ', indexes[ord(string[i])])
        print('start: ', start)
        if indexes[ord(string[i])] >= start:
            print('Entered loop')
            start = indexes[ord(string[i])] + 1
        indexes[ord(string[i])] = i
        max_len = max(max_len, i - start + 1)
    return max_len


if __name__ == '__main__':
    print(solution('abccdcpqwertydacdbbc'))
