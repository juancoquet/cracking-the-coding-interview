from data_structures.linked_list import LinkedList


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


# 2.5 sum lists
def sum_lists(num_list1, num_list2):
    num1, num2 = '', ''
    current = num_list1.head
    while current is not None:
        digit = str(current.data)
        num1 = digit + num1
        current = current.next
    
    current = num_list2.head
    while current is not None:
        digit = str(current.data)
        num2 = digit + num2
        current = current.next

    num1 = int(num1)
    num2 = int(num2)
    result = str(num1 + num2)
    result_ll = LinkedList()
    
    for c in result:
        result_ll.add(int(c))
    
    return result_ll


# 2.6 palindrome
from data_structures.stack import Stack

def palindrome(llist):
    size = llist.size()
    mid = size // 2
    checked = Stack()
    i = 0
    current = llist.head
    while i < mid:
        checked.push(current)
        current = current.next
        i += 1
    if size % 2 == 0:
        checked.push(current)
    current = current.next
    while current:
        if current != checked.pop():
            return False
        current = current.next
    return True


# 2.7 intersection
def intersection(a, b):
    diff = 0
    longer = None
    if a.size() > b.size():
        diff = a.size() - b.size()
        longer = a
    if b.size() > a.size():
        diff = b.size() - a.size()
        longer = b
    
    current_a = a.head
    current_b = b.head

    if a is longer:
        for _ in range(diff):
            current_a = current_a.next
    elif b is longer:
        for _ in range(diff):
            current_b = current_b.next

    while current_a is not current_b:
        current_a = current_a.next
        current_b = current_b.next

    return current_a


# 2.8 loop detection
def loop_detection(ll):
    slow = ll.head
    fast = ll.head.next
    while slow is not fast and fast is not None:
        slow = slow.next
        fast = fast.next.next
    
    if fast is None:
        return None

    curr = ll.head
    visited = []
    while curr not in visited:
        visited.append(curr)
        curr = curr.next
    return curr