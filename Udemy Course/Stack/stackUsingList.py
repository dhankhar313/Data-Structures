class Stack:
    def __init__(self, size):
        self.list = []
        self.size = size

    def __repr__(self):
        # return ' '.join([str(i) for i in self.list[::-1]])
        return ' '.join([str(i) for i in self.list])

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def is_full(self):
        return True if len(self.list) == self.size else False

    def push(self, value):
        if self.is_full():
            print('Stack Overflow')
        else:
            self.list.insert(0, value)

    def pop(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            self.list.pop(0)

    def peek(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            print(self.list[0])


if __name__ == '__main__':
    stack = Stack(5)
    print(stack.is_empty())
    stack.pop()
    stack.push(23)
    stack.push(213)
    stack.push(768)
    print(stack.is_empty())
    print(stack)
    # stack.pop()
    # stack.pop()
    print(stack)
    stack.push(87)
    print(stack)
    stack.peek()
    stack.push(879)
    stack.push(5677)
    print(stack)
