import queue

from data_structures.linked_list import LinkedList
from data_structures.trees import BinaryTree, BinarySearchTree


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


class CustomBinarySearchTree:
    
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


# 4.4 check balanced
def get_height(node):
    if node is None:
        return 0
    if node.height is not None:
        return node.height # assuming modified Node class
    height = 1 + max(get_height(node.left_child), get_height(node.right_child))
    node.height = height
    return height

def check_balanced(node):
    if node is None:
        return True
    left_height = get_height(node.left_child)
    right_height = get_height(node.right_child)
    diff = left_height - right_height
    if not -1 <= diff <= 1:
        return False
    return check_balanced(node.left_child) and check_balanced(node.right_child)


# 4.5 check if binary tree is a BST
def validate_bst(root):
    if root is None:
        return True
        
    left_valid = (root.left_child is None) or (root.left_child < root)
    right_valid = (root.right_child is None) or (root.right_child >= root)
    root_valid = left_valid and right_valid
    if not root_valid:
        return False
        
    l_subtree_valid = validate_bst(root.left_child)
    if not l_subtree_valid:
        return False
    r_subtree_valid = validate_bst(root.right_child)
    if not r_subtree_valid:
        return False
    return l_subtree_valid and r_subtree_valid


# 4.6 find successor in a BST
def find_successor(node):
    if node.right_child is not None:
        return find_min(node.right_child)
    if node.parent is not None: # not root
        if node.is_left_child():
            return node.parent
        if node.is_right_child():
            node.parent.right_child = None # prune node
            successor = find_successor(node.parent)
            node.parent.right_child = node # put back
    else:
        successor = None
    return successor

def find_min(node):
    curr = node
    while curr.left_child is not None:
        curr = curr.left_child
    return curr


# 4.7 build order
class Project:

    def __init__(self, name):
        self.name = name
        self.connected_to = []
        self.visited = False
        self.discovered = None
        self.fully_searched = False
        self.predecessor = None
        self.finished = None

    def add_dependency(self, to_project):
        self.connected_to.append(to_project)


class Graph:

    def __init__(self):
        self.vertices = {}
        self.time = 0

    def add_vertex(self, name):
        vertex = Project(name)
        self.vertices[name] = vertex

    def get_vertex(self, name):
        return self.vertices.get(name)

    def add_edge(self, from_vx, to_vx):
        if from_vx not in self.vertives:
            self.add_vertex(from_vx)
        if to_vx not in self.vertices:
            self.add_vertex(to_vx)
        self.vertices[from_vx].add_dependency(self.vertices[to_vx])

    def dfs(self):
        for vx in self.vertices.values():
            if not vx.visited:
                self.dfs_visit(vx)

    def dfs_visit(self, vertex):
        vertex.visited = True
        self.time += 1
        vertex.discovered = self.time
        for neighbour in vertex.connected_to:
            if not neighbour.visited:
                neighbour.predecdessor = vertex
                self.dfs_visit(neighbour)
        vertex.fully_searached = True
        self.time += 1
        vertex.finished = self.time

    def topological_sort(self):
        self.dfs()
        ordered = [vx for vx in self.vertices.values()]
        ordered.sort(key=lambda x: x.finished)
        return ordered

    
# 4.8 first common ancestor
def dfs(root, target, ignore_left=False, ignore_right=False):
    if root is target:
        return True
    if not ignore_left and root.left_child is not None:
        found_left = dfs(root.left_child, target)
    else:
        found_left = False
    if not ignore_right and root.right_child is not None:
        found_right = dfs(root.right_child, target)
    else:
        found_right = False
    
    return found_left or found_right


def first_common_ancestor(node1, node2):
    ancestor = node1.parent
    ign_l = False
    ign_r = False
    while not dfs(ancestor, node2, ign_l, ign_r):
        last_searched = ancestor
        ancestor = ancestor.parent
        if ancestor.right_child is last_searched:
            ign_r = True
        else:
            ign_r = False
        if ancestor.left_child is last_searched:
            ign_l = True
        else:
            ign_l = False
    return ancestor


# print as binary
num = ((1 << 2) - 1) ^ 0xFF
print(f'{num:08b}')