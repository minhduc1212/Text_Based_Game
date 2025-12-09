from base import Base
import random

class Ocean(Base):
    def __init__(self, name, size, location, description):
        super().__init__(name, size, location, description, children=[], number_children=random.randint(0, 5), parent=None)