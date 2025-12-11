from .stat import Strength

def create_character():    
    strength = Strength("Swordman")
    print(strength.get_value())