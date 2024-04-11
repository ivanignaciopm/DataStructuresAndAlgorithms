# O(log N)
# There are 3 ways of traversing the tree:
# In order, pre order y post order

class BST:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
        
    def insert(self, value):
        
        if (value < self.value):
            if (self.left is None):
                self.left = BST(value, self.depth + 1)
                
            else:
                self.left.insert(value)
        
        else:
            if (self.right is None):
                self.right = BST(value, self.depth + 1)
                
            else:
                self.right.insert(value)
    
    def get_node_by_value(self, value):
        
        if (self.value == value):
            return self
        
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
        
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
        
        else:
            return None
        
    def depth_first_traversal(self):
        
        if(self.left is not None):
            self.left.depth_first_traversal()
        
        print(f"Depth={self.depth}, value={self.value}")
        
        if(self.right is not None):
            self.right.depth_first_traversal()
    