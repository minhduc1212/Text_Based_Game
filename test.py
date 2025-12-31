from src.character import *
from src.character_class import swordman
from src.statistic import *

player = Character("Non", 18, 18, 100, 100, 100, "Human", "Male")

print("What class do you want to be?")
print("1. Swordman")

choice = input("Enter the number of your choice: ")
if choice == "1":
    player.character_class = swordman("Swordman", strength, dexterity, intelligence, mind, luck, vitality, fixed_stat=[], flex_stat=[])
    print(f"You have chosen the {player.character_class.name} class.")
else:
    print("Invalid choice.")

#add 1 point to strength
player.character_class.add_point("strength", 1)
print(f"Strength is now: {player.character_class.strength.point}")

#playerstat
strength_point = player.character_class.strength.point
dexterity_point = player.character_class.dexterity.point
intelligence_point = player.character_class.intelligence.point
mind_point = player.character_class.mind.point
luck_point = player.character_class.luck.point
vitality_point = player.character_class.vitality.point

# Save character data
player.create(strength_point, dexterity_point, intelligence_point, mind_point, luck_point, vitality_point)
