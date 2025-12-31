import json
from src.statistic import *


def load_data(character_class_name: str):
        with open("data/class_stat.json", "r") as f:
            class_data = json.load(f)
            return class_data[character_class_name]

class base_class:
    def __init__(self, name: str, strength: strength, dexterity: dexterity, intelligence: intelligence, mind: mind, luck: luck, vitality: vitality):
        self.name = name
        self.strength = strength("Strength", load_data(name)["Strength"])
        self.dexterity = dexterity("Dexterity", load_data(name)["Dexterity"])
        self.intelligence = intelligence("Intelligence", load_data(name)["Intelligence"])
        self.mind = mind("Mind", load_data(name)["Mind"])
        self.luck = luck("Luck", load_data(name)["Luck"])
        self.vitality = vitality("Vitality", load_data(name)["Vitality"])
    
class swordman(base_class):
    def __init__(self, name: str,  strength, dexterity, intelligence, mind, luck, vitality):
        super().__init__(name, strength, dexterity, intelligence, mind, luck, vitality)       
        