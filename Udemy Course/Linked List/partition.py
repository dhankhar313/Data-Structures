import Single as ll


def partition(lst, num):
    temp_node = lst.head
    smaller = ll.LinkedList()
    larger = ll.LinkedList()
    while temp_node:
        if temp_node.value <= num:
            smaller.append(temp_node.value)
        else:
            larger.append(temp_node.value)
        temp_node = temp_node.next
    temp_node1 = smaller.head
    while temp_node1.next:
        temp_node1 = temp_node1.next
    temp_node1.next = larger.head
    return smaller


lst = ll.LinkedList()
lst.push(45)
lst.push(76)
lst.append(342)
lst.insertAtN(23, 3)
lst.append(87)
lst.push(213)
lst.append(213)
lst.push(87)
lst.insertAtN(23, 1)
print(partition(lst, 100))
