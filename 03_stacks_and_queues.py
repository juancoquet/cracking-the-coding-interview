from data_structures.stack import Stack


# 3.2 stack min
class StackNode():

    def __init__(self, data):
        self.data = data
        self.substack_min = data


class MinStack():

    def __init__(self):
        self.items = []

    @property
    def size(self):
        return len(self.items)

    def push(self, data):
        node = StackNode(data)
        if self.size == 0:
            self.items.append(node)
        else:
            top_node = self.items[-1]
            current_min = top_node.substack_min
            if data > current_min:
                node.substack_min = current_min
            self.items.append(node)

    def pop(self):
        top_node = self.items.pop()
        return top_node.data

    def min(self):
        top_node = self.items[-1]
        return top_node.substack_min


# 3.3 Stack of Plates
class StackOfStacks():

    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [Stack()]

    @property
    def _last_stack(self):
        return self.stacks[-1]

    def push(self, item):
        if self._last_stack.size >= self.threshold:
            self.stacks.append(Stack())
            self.push(item)
        else:
            self._last_stack.push(item)

    def pop(self):
        item = self._last_stack.pop()
        if self._last_stack.size == 0 and len(self.stacks) > 1:
            self.stacks.pop()
        return item

    def pop_at(self, i):
        stack = self.stacks[i]
        item = stack.pop()
        if stack.size == 0 and len(self.stacks) > 1:
            self.stacks.pop(i)

# 3.4 Queue via Stacks
class MyQueue:

    def __init__(self):
        self.main = Stack() # assuming prior existence of Stack class
        self.aux = Stack()
        self.last_op = 'enq'

    def enqueue(self, item):
        if self.last_op == 'deq':
            while not self.main.is_empty():
                transfer = self.main.pop()
                self.aux.push(transfer)
        self.aux.push(item)
        self.last_op = 'enq'

    def dequeue(self):
        if self.last_op == 'enq':
            while not self.aux.is_empty():
                transfer = self.aux.pop()
                self.main.push(transfer)
        self.last_op = 'deq'
        return self.main.pop()

    def size(self):
        return self.main.size()

    def is_empty(self):
        return self.main.is_empty()