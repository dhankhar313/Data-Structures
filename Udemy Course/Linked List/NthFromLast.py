import Single as ll


def kth_from_last(lst, n):
    temp_node = lst.head
    count = 0
    while temp_node:
        count += 1
        temp_node = temp_node.next
    position = count - n + 1
    temp_node = lst.head
    for i in range(position - 1):
        temp_node = temp_node.next
    return temp_node.value


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
print(kth_from_last(lst, 3))
print(kth_from_last(lst, 7))
print(kth_from_last(lst, 9))
print(kth_from_last(lst, 1))
