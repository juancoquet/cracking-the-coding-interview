import queue

from data_structures.linked_list import LinkedList


# 4.1 route between nodes
def route_exists(start, target):
    if bfs(start, target):
        path = [target,]
        current = target
        while current.predecessor is not None:
            path.append(current.predecessor)
        path.reverse()
        return(path)
    return False


def bfs(start, target):
    to_search = queue()
    start.visited = True
    to_search.enqueue(start)
    while to_search.size > 0:
        current = to_search.dequeue()
        for neighbour in current.connected_to:
            if not neighbour.visited and not neighbour.fully_searched:
                neighbour.visited = True
                to_search.enqueue(neighbour)
                neighbour.predecessor = current
                if neighbour == target:
                    return True
        current.fully_searched = True
    return False


# 4.2 minimal tree
class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_left_child(self, data):
        new_node = Node(data)
        self.left_child = new_node

    def add_right_child(self, data):
        new_node = Node(data)
        self.right_child = new_node

    def __iter__(self):
        if self:
            yield self
            if self.left_child:
                for node in self.left_child:
                    yield node
            if self.right_child:
                for node in self.right_child:
                    yield node


class BinarySearchTree:
    
    def __init__(self, root=None):
        self.root = root

    def put(self, data):
        print('putting:', data)
        if self.root:
            self._put(data, self.root)
        else:
            self.root = Node(data)


    def _put(self, data, current_node):
        if data < current_node.data:
            if current_node.left_child:
                self._put(data, current_node.left_child)
            else:
                current_node.add_left_child(data)
        else:
            if current_node.right_child:
                self._put(data, current_node.right_child)
            else:
                current_node.add_right_child(data)

    def insert_ordered_list(self, ol):
        if len(ol) == 1:
            self.put(ol[0])
            return
        elif len(ol) < 1:
            return
        midpoint = len(ol) // 2
        mid_el = ol[midpoint]
        self.put(mid_el)
        left = ol[:midpoint]
        right = ol[midpoint + 1:]
        self.insert_ordered_list(left)
        self.insert_ordered_list(right)

    def __iter__(self):
        return self.root.__iter__()


# 4.3 list of depths
def create_depth_dict(node, depth=0, node_depths={}):
    depth_exists = node_depths.get(depth)
    if not depth_exists:
        node_depths[depth] = []
        
    node_depths[depth].append(node)
    
    if node.left_child:
        create_depth_dict(node.left_child, depth+1, node_depths)
    if node.right_child:
        create_depth_dict(node.right_child, depth+1, node_depths)
    return node_depths

def dict_to_linked_lists(node_depths):
    lls = []
    for depth, nodes in node_depths.items():
        ll = LinkedList() # assuming existence of class
        for node in nodes:
            ll.add(node)
        lls.append(ll)
    return lls