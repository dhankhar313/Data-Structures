class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        new_node = self.head
        count = 1
        while new_node.next:
            count += 1
            new_node = new_node.next
        return count

    def __repr__(self):
        new_node = self.head
        nodes = []
        while new_node:
            if new_node is self.head:
                nodes.append(f"[Head: {new_node.data}]")
            elif new_node.next is None:
                nodes.append(f"[Tail: {new_node.data}]")
            else:
                nodes.append(f"[{new_node.data}]")
            new_node = new_node.next
        return f"{'-> '.join(nodes)} Length: {len(self)}"

    def insertAt1(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(self)
            return
        new_node1 = self.head
        new_node1.prev = new_node
        new_node.next = self.head
        self.head = new_node
        print(self)

    def insertAtLast(self, data):
        new_node = Node(data)
        new_node1 = self.head
        while new_node1.next:
            new_node1 = new_node1.next
        new_node1.next = new_node
        new_node.prev = new_node1
        print(self)

    def insertAtN(self, data, position):
        new_node = Node(data)
        new_node1 = self.head
        for i in range(position - 2):
            new_node1 = new_node1.next
        new_node.next = new_node1.next
        new_node.prev = new_node1
        new_node1.next.prev = new_node
        new_node1.next = new_node
        print(self)

    def print_reverse_list(self):
        new_node = self.head
        while new_node.next:
            new_node = new_node.next
        while new_node:
            print(new_node.data, end=" ")
            new_node = new_node.prev


if __name__ == "__main__":
    obj = DoublyLinkedList()
    obj.insertAt1(10)
    obj.insertAtLast(30)
    obj.insertAt1(201)
    obj.insertAtN(312, 3)
    obj.insertAtLast(34)
    obj.insertAtN(23, 2)
    obj.insertAtN(50, 5)
    obj.insertAt1(300)
    obj.print_reverse_list()
