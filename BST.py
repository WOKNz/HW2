class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree


class BinarySearchTree:
    def default_key(x):  # default key:, key used to sort on different fields
        return x

    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, this_node):
        if value < this_node.value:
            if this_node.left_child is None:
                this_node.left_child = Node(value)
                this_node.left_child.parent = this_node  # Setting Parent
            else:
                self._insert(value, this_node.left_child)
        elif value > this_node.value:
            if this_node.right_child is None:
                this_node.right_child = Node(value)
                this_node.right_child.parent = this_node  # Setting Parent
            else:
                self._insert(value, this_node.right_child)
        else:
            print("Value already in tree!")

    # def print_tree(self):
    #     if self.root is not None:
    #         self._print_tree(self.root)
    #
    # def _print_tree(self, this_node):
    #     if this_node is not None:
    #         self._print_tree(this_node.left_child)
    #         print(str(this_node.value))
    #         self._print_tree(this_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, this_node, cur_height):
        if this_node is None: return cur_height
        left_height = self._height(this_node.left_child, cur_height + 1)
        right_height = self._height(this_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value, key = default_key()):
        if self.root is not None:
            return self._find(value, self.root, key=key)
        else:
            return None

    def _find(self, value, this_node, key):
        if value == this_node.value:
            return this_node
        elif key(value) < key(this_node.value) and this_node.left_child is not None:
            return self._find(value, this_node.left_child)
        elif key(value) > key(this_node.value) and this_node.right_child is not None:
            return self._find(value, this_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        ## -----
        # Improvements since prior lesson

        # Protect against deleting a node not found in the tree
        if node is None or self.find(node.value) is None:
            print("Node to be deleted not found in the tree!")
            return None
        ## -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child is not None: num_children += 1
            if n.right_child is not None: num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent is not None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent is not None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, this_node):
        if value == this_node.value:
            return True
        elif value < this_node.value and this_node.left_child is not None:
            return self._search(value, this_node.left_child)
        elif value > this_node.value and this_node.right_child is not None:
            return self._search(value, this_node.right_child)


return False
