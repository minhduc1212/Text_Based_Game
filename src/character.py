import json

class Character:
    def __init__(self, name: str, age: int, level: int, health: int, mana: int, stamina: int, race: str, gender: str):
        self.name = name
        self.age = age
        self.level = level
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.race = race
        self.gender = gender
    def create(self):
        data = {
            "name": self.name,
            "age": self.age,
            "level": self.level,
            "health": self.health,
            "mana": self.mana,
            "stamina": self.stamina,
            "race": self.race,
            "gender": self.gender
        }
        with open(f"data/{self.name}.json", "w") as f:
            json.dump(data, f)

