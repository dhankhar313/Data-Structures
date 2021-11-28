class Queue:
    def __init__(self, size):
        self.lst = []
        self.size = size

    def __repr__(self):
        return ' '.join([str(i) for i in self.lst])

    def is_empty(self):
        return True if len(self.lst) == 0 else False

    def is_full(self):
        return True if len(self.lst) == self.size else False

    def enqueue(self, value):
        if self.is_full():
            print('Stack Overflow')
        else:
            self.lst.append(value)
        print(self)

    def dequeue(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            self.lst.pop()
        print(self)

    def peek(self):
        print(self.lst[0])


if __name__ == '__main__':
    queue = Queue(10)
    print(queue.is_empty())
    queue.enqueue(212)
    queue.dequeue()
    queue.enqueue(445)
    queue.enqueue(45)
    queue.enqueue(5)
    queue.enqueue(9090)
    queue.dequeue()
    queue.peek()