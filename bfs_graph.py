def bfs(graph, start_vert, target_val):
  path = [start_vert]
  vertex_and_path = [start_vert, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
      # Add your code here:
        if neighbor is target_val:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])
 

# Leave this for testing:
the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }
print(bfs(the_most_dangerous_graph, "piranhas", "bees"))