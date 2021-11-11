# User function Template for python3

class Solution:
    def findSubString(self, str):
        char = set(list(str))
        min_len = len(str)
        min_str = ''
        print(char)
        for i in range(len(str)):
            for j in range(i + 1, len(str) + 1):
                temp = str[i:j]
                print('Current string: ', temp)
                count = 0
                temp1 = set(list(temp))
                for x in char:
                    if x in temp1:
                        count += 1
                if count == len(char) and len(temp) < min_len:
                    print('All found in the string!!')
                    min_len = len(temp)
                    min_str = temp

        return len(min_str)


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
