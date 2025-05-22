class Node:
    def __init__(self, name, f):
        self.name = name          
        self.f = f                
        self.parent = None        
        self.children = []

    def add_child(self, child):
        self.children.append(child)