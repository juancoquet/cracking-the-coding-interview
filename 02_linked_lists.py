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

# 2.3 delete middle node
def delete_middle_node(target_node):
    if target_node is None:
        raise ValueError("Target node is None")
    if target_node.next is None:
        raise ValueError("Target node is the last node")
    target_node.data = target_node.next.data
    target_node.next = target_node.next.next

# 2.4 partition
def partition(llist, partition):
    if llist.head < partition: # assuming comparison operators set up
        partition_front = llist.head
    else:
        partition_front = None
    
    runner = llist.head.next
    predecessor = llist.head
    while runner is not None:
        if runner < partition:
            if partition_front is None:
                temp = runner.next
                predecessor.next = runner.next
                runner.next = llist.head
                llist.head = runner
                partition_front = runner
                runner = temp
            else:
                temp = runner.next
                predecessor.next = runner.next
                runner.next = partition_front.next
                partition_front.next = runner
                partition_front = runner
                runner = temp
            if predecessor.next is not runner:
                predecessor = predecessor.next
        else:
            runner = runner.next
            predecessor = predecessor.next
    return llist

llist = LinkedList()
llist.add(1)
llist.add(9)
llist.add(3)
llist.add(3)
llist.add(4)
llist.add(2)
llist.add(1)
llist.add(6)
llist.add(12)
print(llist)