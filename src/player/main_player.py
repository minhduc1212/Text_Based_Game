from src.core import port_stat_value #the way to import from src
import json

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
    with open("player.json", "w") as f:
        json.dump(main_player, f, indent=4)


