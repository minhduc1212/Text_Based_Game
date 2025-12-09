from base import Base

class Continent(Base):
    def __init__(self, name, size, location, description):
        super().__init__(name, size, location, description, children=[], number_children=10, parent=None)