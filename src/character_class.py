import json

class base_class:
    def __init__(self, name: str, fixed_stat, flex_stat):
        self.name = name
        self.fixed_stat = []
        self.flex_stat = []
        
    def add_point(self, stat: str):
        if stat in self.flex_stat:
            stat.point += 1
    
    def lose_point(self, stat: str):
        if stat in self.flex_stat:
            stat.point -= 1
    
    def load_data(self):
        with open("class_stat.json", "r") as f:
            class_data = json.load(f)
            return class_data[self.name]
    
    

class swordman(base_class):
    def __init__(self, name: str, fixed_stat, flex_stat):
        super().__init__(name, fixed_stat, flex_stat)       
        self.fixed_stat = ["mind", "intelligence"]
        self.flex_stat = ["strength", "dexterity", "vitality", "luck"]