# This recursive method uses D&Q
# DFS uses a stack
# Tuples are immutable lists
# They provide efficiency + hashability

def dfs(root, target, path=()):
    path = path + (root,)
    
    if root.value==target:
        return path
    
    for child in root.children:
        path_found = dfs(child, target, path)
        
        if path_found is not None:
            return path_found
        
    return None 