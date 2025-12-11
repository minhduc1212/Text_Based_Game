import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "start_stat.json")

def get_stat(name: str, hero_class: str):
    with open(JSON_PATH, "r") as f:
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

    #setter and getter
    def get_value(self):
        return self.value

    def set_value(self, value: int):
        self.value = value

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


    
