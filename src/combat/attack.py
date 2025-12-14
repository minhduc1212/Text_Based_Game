class attack:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type
        
            
class normal_attack(attack):
    def __init__(self, name, damage, type):
        super().__init__(name, damage, type)
    def begin(self, target):
        print(self.name + " attack " + target["name"])
        target["hp"] -= self.damage

    
