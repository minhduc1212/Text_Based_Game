import json
from src.statistic import *


def load_data(character_class_name: str):
        with open("data/class_stat.json", "r") as f:
            class_data = json.load(f)
            return class_data[character_class_name]

class base_class:
    def __init__(self, name: str, strength, dexterity, intelligence, mind, luck, vitality, fixed_stat, flex_stat):
        self.name = name
        self.strength = strength("Strength", load_data(name)["Strength"])
        self.dexterity = dexterity("Dexterity", load_data(name)["Dexterity"])
        self.intelligence = intelligence("Intelligence", load_data(name)["Intelligence"])
        self.mind = mind("Mind", load_data(name)["Mind"])
        self.luck = luck("Luck", load_data(name)["Luck"])
        self.vitality = vitality("Vitality", load_data(name)["Vitality"])
        self.fixed_stat = fixed_stat
        self.flex_stat = flex_stat
        
    def add_point(self, stat_name, points: int):
        if stat_name in self.flex_stat:
            getattr(self, stat_name).add_point(points)
        else:
            print(f"Cannot add points to {stat_name}. It is a fixed stat.")
    
class swordman(base_class):
    def __init__(self, name: str,  strength, dexterity, intelligence, mind, luck, vitality, fixed_stat, flex_stat):
        super().__init__(name, strength, dexterity, intelligence, mind, luck, vitality, fixed_stat, flex_stat)       
        self.fixed_stat = ["mind", "intelligence"]
        self.flex_stat = ["strength", "dexterity", "vitality", "luck"]