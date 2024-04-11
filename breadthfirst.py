from collections import deque 

def bfs(root_node, goal_value):
    # Frontier queue
    path_queue = deque()
    
    # Add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
    
    while path_queue:
        
        # Pop one node
        current_path = path_queue.pop()
        current_node = current_path[-1]
        
        # Evaluate it
        if current_node.value == goal_value:
            return current_path

        # Add all the children to the frontier queue
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)
    
    return None 