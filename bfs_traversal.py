tree={
       'A':['B','C'],
       'B':['D','E'],
       'C':['F','G'],
       'D':[ ],
       'E':[ ],
       'F':[ ],
       'G':[ ],
       }
start=input("Enter the starting node: ")
def bfs_connected_component(tree):
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours=tree[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited 
print("\nHere's the nodes of the tree visited by BFS:\n",bfs_connected_component(tree))          
