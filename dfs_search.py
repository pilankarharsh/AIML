tree={'A':['B','C'], 'B':['D','E'], 'C':['F','G'], 'D':[], 'E':[], 'F':[], 'G':[]}

start = input("Enter Start State: ")
goal = input("Enter Goal State: ")

def dfs(tree):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                return visited

            neighbours = tree.get(node,[])
            for i in neighbours:
                stack.append(i)
    print("State not found!!")
    return None

print("Traversal DFS: ", dfs(tree))
