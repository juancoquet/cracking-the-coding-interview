class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if not previous:
            self.head = current.next
        else:
            previous.next = current.next
        return current.data
    
    def append(self, item):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(item)
    
    def insert(self, index, item):
        current = self.head
        previous = None
        idx = 0
        while idx != index:
            previous = current
            current = current.next
            idx += 1
        new_node = Node(item)
        new_node.next = current
        if previous:
            previous.next = new_node
        else:
            self.head = new_node


    def index(self, item):
        current = self.head
        idx = 0
        while current:
            if current.data == item:
                return idx
            else:
                current = current.next
                idx += 1

    def pop(self):
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        if previous:
            previous.next = None
        else:
            self.head = None
        return current.data