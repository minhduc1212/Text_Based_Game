#the base for to create area and add them to the world
class Base:
    def __init__(self, name, size, location, description, children, number_children, parent=None):
        self.name = name
        self.size = int(size)
        self.location = location
        self.description = description
        self.number_children = number_children
        self.children = []
        self.parent = parent
    #add children
    def add_children(self, child):
        self.children.append(child)
        child.parent = self    
        
        
        
        