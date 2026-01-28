import json
import os
from src.statistic import *
from src.character_class import *


class Character:
    def __init__(self, name: str, age: int, level: int, health: int, mana: int, stamina: int, race: str, gender: str, character_class=None, stats = None):
        self.name = name
        self.age = age
        self.level = level
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.race = race
        self.gender = gender
        self.character_class = character_class
        self.stats = stats 


    def create_stats(self, strength_point: int, dexterity_point: int, intelligence_point: int, mind_point: int, luck_point: int, vitality_point: int):
        self.stats = {
            "Strength": strength_point,
            "Dexterity": dexterity_point,
            "Intelligence": intelligence_point,
            "Mind": mind_point,
            "Luck": luck_point,
            "Vitality": vitality_point
        }
        return self.stats
    def save(self):
        data = {
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "health": self.health,
            "mana": self.mana,
            "stamina": self.stamina,
            "race": self.race,
            "gender": self.gender,
            "character_class": self.character_class.name,
            "stats": self.stats 
        }  
        if not os.path.exists("data"):
            os.makedirs("data")
        with open(f"data/{self.name}.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
    def create(self, strength_point, dexterity_point, intelligence_point, mind_point, luck_point, vitality_point):
        data = {
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "health": self.health,
            "mana": self.mana,
            "stamina": self.stamina,
            "race": self.race,
            "gender": self.gender,
            "character_class": self.character_class.name,
            "stats": self.create_stats(strength_point, dexterity_point, intelligence_point, mind_point, luck_point, vitality_point)          
        }
        self.save()

