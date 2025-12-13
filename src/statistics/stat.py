import json
import os


def get_stat(name: str, hero_class: str):
    with open("data/base_stat.json", "r") as f:
        data = json.load(f)
    return data[hero_class][name] 


class BaseStat:
    #constuctor
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def increase(self, amount: int):
        self.value += amount

    def decrease(self, amount: int):
        self.value -= amount

    def __str__(self):
        return f"{self.name}: {self.value}"

"""
Stat:   Strength (Sức Mạnh)
        Dexterity (Linh Hoạt)
        Mind or Intelligent
"""
class Strength(BaseStat):
    def __init__(self, hero_class: str):
        value = get_stat("Strength", hero_class)
        super().__init__("Strength", value)
        self.hero_class = hero_class
        
class Dexterity(BaseStat):
    def __init__(self, hero_class: str):
        value = get_stat("Dexterity", hero_class)
        super().__init__("Dexterity", value)
        self.hero_class = hero_class

class Intelligence(BaseStat):
    def __init__(self, hero_class: str):
        value = get_stat("Intelligence", hero_class)
        super().__init__("Intelligence", value)
        self.hero_class = hero_class




    
