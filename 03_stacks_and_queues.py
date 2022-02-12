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

