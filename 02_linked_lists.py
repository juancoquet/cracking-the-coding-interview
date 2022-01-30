from data_structures.linked_list import LinkedList

llist = LinkedList()
llist.add(1)
llist.add(9)
llist.add(3)
llist.add(3)
llist.add(4)
llist.add(2)
llist.add(1)
llist.add(6)
llist.add(4)

def remove_dups(linked_list):
    exists = {}
    current = linked_list.head
    previous = None
    while current != None:
        if current.data not in exists:
            exists[current.data] = 1
            previous = current
            current = current.next
        else:
            previous.next = current.next
            current.next = None
            current = previous.next

