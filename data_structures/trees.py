class BinaryTree:

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            insert_node = BinaryTree(new_node)
            insert_node.left_child = self.left_child
            self.left_child = insert_node
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            insert_node = BinaryTree(new_node)
            insert_node.right_child = self.right_child
            self.right_child = insert_node

    # comparison operators
    def __eq__(self, other):
         return self.key == other

    def __ne__(self, other):
        return self.key != other

    def __lt__(self, other):
        return self.key < other

    def __le__(self, other):
        return self.key <= other

    def __gt__(self, other):
        return self.key > other

    def __ge__(self, other):
        return self.key >= other



class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
            else:
                return None
        else:
            return None
    
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf(): # current_node has no children
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else: # current_node has one child
            if current_node.has_left_child(): # current_node only has left child
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else: # current_node is root
                    current_node.replace_node_data(
                        key=current_node.left_child.key,
                        value=current_node.left_child.value,
                        left_child=current_node.left_child.left_child,
                        right_child=current_node.left_child.right_child
                    )
            else: # current_node only has right child
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else: # current_node is root
                    current_node.replace_node_data(
                        key=current_node.right_child.key,
                        value=current_node.right_child.value,
                        left_child=current_node.right_child.left_child,
                        right_child=current_node.right_child.right_child
                    )


class TreeNode:

    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.balance_factor = 0

    def __iter__(self):
        if self:
            if self.has_left_child():
                for node in self.left_child:
                    yield node
            yield self
            if self.has_right_child():
                for node in self.right_child:
                    yield node

    # comparison operators
    def __eq__(self, other):
         return self.key == other

    def __ne__(self, other):
        return self.key != other

    def __lt__(self, other):
        return self.key < other

    def __le__(self, other):
        return self.key <= other

    def __gt__(self, other):
        return self.key > other

    def __ge__(self, other):
        return self.key >= other

    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child
    
    def has_both_children(self):
        return self.left_child and self.right_child
    
    def update_left_child(self, new_node):
        self.left_child = new_node
        if new_node:
            new_node.parent = self
    
    def update_right_child(self, new_node):
        self.right_child = new_node
        if new_node:
            new_node.parent = self

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
    
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child(): # has left child and is left child
                    self.parent.left_child = self.left_child
                else: # has left child and is right child
                    self.parent.right_child= self.left_child
                self.left_child.parent = self.parent
            else: # has right child
                if self.is_left_child(): # has right child and is left child
                    self.parent.left_child = self.right_child
                else: # has right child and is right child
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
    
    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else: # is right child
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node


class AVLTree(BinarySearchTree):

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.update_left_child(TreeNode(key, value, parent=current_node))
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, orig_root):
        new_root = orig_root.right_child
        orig_root.right_child = new_root.left_child
        if new_root.left_child != None:
            new_root.left_child.parent = orig_root
        new_root.parent = orig_root.parent
        if orig_root.is_root():
            self.root = new_root
        else:
            if orig_root.is_left_child():
                    orig_root.parent.left_child = new_root
            else:
                orig_root.parent.right_child = new_root
        new_root.left_child = orig_root
        orig_root.parent = new_root
        orig_root.balance_factor = orig_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(orig_root.balance_factor, 0)

    def rotate_right(self, orig_root):
        new_root = orig_root.left_child
        orig_root.left_child = new_root.right_child
        if new_root.right_child != None:
            new_root.right_child.parent = orig_root
        new_root.parent = orig_root.parent
        if orig_root.is_root():
            self.root = new_root
        else:
            if orig_root.is_left_child():
                    orig_root.parent.left_child = new_root
            else:
                orig_root.parent.right_child = new_root
        new_root.right_child = orig_root
        orig_root.parent = new_root
        orig_root.balance_factor = orig_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(orig_root.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)