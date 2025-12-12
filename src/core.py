#the core to manage all package and function

#manage the stat with class "None"
from .statistics.stat import *

def port_stat_value(hero_class: str):
    strength = Strength(hero_class)
    dexterity = Dexterity(hero_class)
    intelligence = Intelligence(hero_class)
    return strength.value, dexterity.value, intelligence.value