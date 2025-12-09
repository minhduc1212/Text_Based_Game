from base import Base
import random

class World(Base):
    def __init__(self, name, size, location, description):
        super().__init__(name, size, location, description, children=[], number_children=random.randint(7, 13), parent=None)
    

        