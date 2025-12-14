from src.world.create import *
from src.player.main_player import *
from src.combat.attack import *

create_player("Non", "None")

player_data = load_player()
player_name = get_player_data("name")


ogre_data = {
    "name": "Ogre",
    "class": "None",
    "hp": 100,
    "stat": {
        "strength": 10,
        "dexterity": 10,
        "intelligence": 10
    }
}

attack = normal_attack(player_name, 15, "physical")

while True:
    if ogre_data["hp"] <= 0:
        print("You won!")
        break
    else:
        attack.begin(ogre_data)
        print(ogre_data["hp"])