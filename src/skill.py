class attack:
    def __init__(self, name, damage, target):
        self.name = name
        self.damage = damage
        self.target = target
        
    def start_attack(self):
        print(f"{self.name} deals {self.damage} damage to {self.target.name}.")
        self.target.health -= self.damage   
    
class NormalAttack(attack):
    def __init__(self, name, damage, target):
        super().__init__("Normal Attack", damage, target)