def longestPalindrome(string):
    freq = {}
    max_len = 0
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    for i in freq.keys():
        count = freq.get(i)
        if count >= 2:
            max_len += count if count % 2 == 0 else count - 1
    return max_len + 1


if __name__ == '__main__':
    print(longestPalindrome('abdccdceeebebc'))
