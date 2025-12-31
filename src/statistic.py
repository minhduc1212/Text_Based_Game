class base_stat:
    def __init__(self, name: str, point: int):
        self.name = name
        self.point = point
        
    def add_point(self, point: int):
        self.point += point
    def lose_point(self, point: int):
        self.point -= point
        
class strength(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)
        
class dexterity(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)

class intelligence(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)

class mind(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)
        
class luck(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)

class vitality(base_stat):
    def __init__(self, name: str, point: int):
        super().__init__(name, point)
    