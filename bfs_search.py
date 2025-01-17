tree={
   	'A':['B','C'],
   	'B':['D','E'],
   	'C':['F','G'],
   	'D':[ ],
   	'E':[ ],
   	'F':[ ],
   	'G':[ ],
   	}
start=input("Enter the starting state: ")
goal=input("Enter the goal state: ")
def bfs(tree):
	open=[start]
	close=[]
	if start==goal:
    	print("\nState Found at Start")
        return open
	close.append(start)
	while open:
    		node=open.pop(0)
    	neighbour=tree[node]
    	for i in neighbour:
           	open.append(i)
           	close.append(i)
           	if i==goal:
              	return close
	print("Goal node does not exist")
print("\nBFS Traversal:\n",bfs(tree))
