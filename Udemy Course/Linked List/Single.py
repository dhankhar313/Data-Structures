class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp_node = self.head
        values = []
        while temp_node:
            values.append(str(temp_node.value))
            temp_node = temp_node.next
        return '->'.join(values)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(self)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            # print(self)
            return

        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node
        del temp_node
        # print(self)

    def insertAtN(self, value, position):
        if position == 0:
            self.push(value)
            return
        temp_node = self.head
        new_node = Node(value)
        for i in range(position - 2):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        print(self)

    def pop(self):
        temp_node = self.head
        while temp_node.next.next:
            temp_node = temp_node.next
        temp_node1 = temp_node.next
        temp_node.next = None
        del temp_node1.next
        print(self)

    def removeAt0(self):
        temp_node = self.head
        self.head = temp_node.next
        del temp_node
        print(self)

    def removeAtN(self, position):
        if position == 0:
            self.removeAt0()
        temp_node = self.head
        for i in range(position - 2):
            temp_node = temp_node.next
        temp_node1 = temp_node.next
        temp_node.next = temp_node.next.next
        del temp_node1
        print(self)


if __name__ == '__main__':
    lst = LinkedList()
    lst.push(50)
    lst.push(10)
    lst.append(215)
    lst.append(28)
    lst.push(32)
    lst.insertAtN(100, 3)
    lst.insertAtN(123, 0)
    lst.pop()
    lst.pop()
    lst.removeAt0()
    lst.removeAtN(3)
    lst.removeAtN(0)
