import math

class Node:
    def __init__(self, name, f):
        self.name = name          
        self.f = f                
        self.parent = None        
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def rbfs(node, goal_name, f_limit):
    print(f"Visiting: {node.name} with f = {node.f} and limit = {f_limit}")

    if node.name == goal_name:
        return node, 0

    if not node.children:
        return None, math.inf 

    while True:
        node.children.sort(key=lambda x: x.f)
        best = node.children[0]

        if best.f > f_limit:
            return None, best.f

        alt_f = node.children[1].f if len(node.children) > 1 else math.inf
        best.parent = node

        result, best.f = rbfs(best, goal_name, min(f_limit, alt_f))
        if result is not None:
            return result, best.f


#----------------Define Graph----------------#
A = Node("A", 100)
B = Node("B", 95)
C = Node("C", 110)
D = Node("D", 115)  
E = Node("E", 118)
F = Node("F", 120)
G = Node("G", 109)
H = Node("H", 114)
K = Node("K", 120)
L = Node("L", 125)
M = Node("M", 122)
N = Node("N", 130)
#childs
A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
C.add_child(G)
C.add_child(H)
H.add_child(K)
H.add_child(L)
K.add_child(M)
K.add_child(N)
#--------------------------------------------#


goal, _ = rbfs(A, "M", math.inf)

if goal:
    path = []
    while goal:
        path.append(goal.name)
        goal = goal.parent
    path.reverse()
    print("Path to goal:", " -> ".join(path))
else:
    print("No path found.")