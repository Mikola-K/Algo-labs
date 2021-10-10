class Tree: 
    
    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True

    def delete(self, value):
        pass


    def max_value(self):
        pass

    def min_value(self):
        pass

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        print(node.value, end = " ")
        if node.left:
            self._print_tree(node.left)
        if node.right:
            self._print_tree(node.right)

    # def _insert_with_search(self, current_nove, value):
    #     found_node =  self._search(current_nove, value) 

        # 2 scenarios
        # scenatio 1 - no such value in Tree
        #found_node_parent 

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        return self._insert(self.root, value)
    
    def _insert(self, current_node, value):
        
        if value > current_node.value:
            #add to the right
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            return self._insert(current_node.right, value)
           # current_node.right = Node(value, current_node)
        else:
            #add to the left
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)

    def _search(self, node_to_check, value):
        if (node_to_check == None) or (node_to_check.value == value):
            return node_to_check
        
        if value > node_to_check.value:
            return self._search(node_to_check.right,value)
        else:
            #check for presence
            return self._search(node_to_check.left, value)

class Node:

    def __init__(self, value, parent = None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value

tree = Tree()
tree.insert(10)
tree.insert(8)
tree.insert(6)

print (tree.search(10))
print (tree.search(8))
print (tree.search(6))
print (tree.search(5))

tree.print_tree()
