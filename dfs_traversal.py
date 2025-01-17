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
def dfs(tree):
	visited=[]
	stack=[start]
	while stack:
    	node=stack.pop()
    	if node not in visited:
        	visited.append(node)
        	neighbours=tree[node]
        	for i in neighbours:
            	stack.append(i)
	return visited
print("\nDFS Traversal:\n",dfs(tree))      