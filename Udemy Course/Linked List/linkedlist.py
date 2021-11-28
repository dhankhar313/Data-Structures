class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node data: {self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next
        return f"{'-> '.join(nodes)} Length: {len(self)}"

    def __len__(self):
        new_node = self.head
        count = 1
        while new_node.next:
            count += 1
            new_node = new_node.next
        return count

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(self)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = None
        new_node1 = self.head
        while new_node1.next:
            new_node1 = new_node1.next
        new_node1.next = new_node
        print(self)

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            self.push(data)
            return

        new_node1 = self.head
        for i in range(position - 2):
            new_node1 = new_node1.next
        new_node.next = new_node1.next
        new_node1.next = new_node
        print(self)

    def pop(self):
        new_node = self.head
        for i in range(len(self) - 2):
            new_node = new_node.next
        new_node1 = new_node.next
        new_node.next = new_node1.next
        del new_node1
        print(self)

    def removeAt0(self):
        new_node = self.head
        self.head = new_node.next
        del new_node
        print(self)

    def removeAtn(self, position):
        new_node = self.head
        if position == 0:
            self.removeAt0()
            return
        for i in range(position - 2):
            new_node = new_node.next
        new_node1 = new_node.next
        new_node.next = new_node1.next
        del new_node1
        print(self)

    def split_list(self, l_list):
        mid = len(l_list) // 2
        initial_head = self.head
        new_node = self.head
        left = LinkedList()
        right = LinkedList()
        for i in range(len(l_list)):
            if i < mid:
                left.append(new_node.data)
            else:
                right.append(new_node.data)
            new_node = new_node.next
        print("LEFT: ", left)
        print("RIGHT: ", right)
        self.head = initial_head
        return left, right

    def reverse(self):
        # Actually reverses the list instead of just printing from tail end
        curr = self.head
        prev = None
        while curr:
            tail = curr.next
            curr.next = prev
            prev = curr
            curr = tail
        self.head = prev
        print(self)

    @staticmethod
    def recursive_reverse_print(head):
        # Doesn't actually reverse the list, Just prints it from tail end
        if not head:
            return
        LinkedList.recursive_reverse_print(head.next)
        print(head.data, end=" ")


if __name__ == "__main__":
    obj = LinkedList()
    obj.push(15)
    obj.push(20)
    obj.push(76)
    obj.push(12)
    obj.append(75)
    obj.append(98)
    obj.insert(0, 999)
    obj.insert(1, 7878)
    obj.insert(8, 1714)
    # obj.split_list(obj)
    # print(obj)
    obj.reverse()
    print("Reversed: ", end="")
    LinkedList.recursive_reverse_print(obj.head)
    print('\n')
    obj.pop()
    obj.removeAtn(1)
    obj.removeAt0()
    obj.removeAt0()
