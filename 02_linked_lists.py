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


# 2.1 remove duplicates
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


# 2.2 kth to last
def size(linked_list):
	count = 0
	i = 0
	indexed = {}
	current = linked_list.head
	while current is not None:
		count += 1
		indexed[i] = current
		i += 1
		current = current.next
	return count, indexed

def get_kth_to_last(linked_list, k):
	count, indexed = size(linked_list)
	if k > count:
		raise IndexError("Index out of range")
	if k < 1:
		raise IndexError("Index must be greater than 0")
	i = count - k
	return indexed[i]

















for item in llist:
    print(item, end=", ")
