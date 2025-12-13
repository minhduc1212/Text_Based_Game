from src.core import port_stat_value #the way to import from src
import json

with open("data/player.json", "r") as f:
    player_data = json.load(f)

def create_player(name: str, hero_class: str):
    strength, dexterity, intelligence = port_stat_value(hero_class)
    main_player = {
        "name": name,
        "class": hero_class,
        "stat": {
            "strength": strength,
            "dexterity": dexterity,
            "intelligence": intelligence
        }
    }
    
    #save to player.json
    with open("data/player.json", "w") as f:
        json.dump(main_player, f, indent=4)
        
def get_player_data(data: str):
    return player_data[data]

def get_player_stat(stat: str):
    return player_data["stat"][stat]




