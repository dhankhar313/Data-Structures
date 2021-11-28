class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.lst = LinkedList()

    def __repr__(self):
        temp_node = self.lst.head
        values = []
        while temp_node:
            values.append(str(temp_node.value))
            temp_node = temp_node.next
        return '->'.join(values)

    def is_empty(self):
        return True if self.lst.head is None else False

    def push(self, value):
        temp_node = Node(value)
        temp_node.next = self.lst.head
        self.lst.head = temp_node

    def pop(self):
        temp_node = self.lst.head
        self.lst.head = temp_node.next
        del temp_node

    def peek(self):
        return self.lst.head.value


stack = Stack()
print(stack.is_empty())
stack.push(512)
stack.push(424)
stack.push(21)
stack.push(1)
print(stack)
stack.pop()
print(stack)
stack.push(19090)
print(stack)
print(stack.peek())
