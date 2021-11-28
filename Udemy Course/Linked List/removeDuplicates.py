import Single as ll


def removeDuplicates(lst):
    temp = lst.head
    vals = []
    while temp.next:
        if temp.next.value not in vals:
            vals.append(temp.next.value)
            temp = temp.next
        else:
            temp.next = temp.next.next
    return lst


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
print(removeDuplicates(lst))
