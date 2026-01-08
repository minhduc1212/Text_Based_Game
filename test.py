from src.character import *
from src.character_class import swordman
from src.statistic import *
from src.start import init_add_stat_points


player = Character("Non", 18, 18, 100, 100, 100, "Human", "Male")

print("What class do you want to be?")
print("1. Swordman")

choice = input("Enter the number of your choice: ")
if choice == "1":
    player.character_class = swordman("Swordman", strength, dexterity, intelligence, mind, luck, vitality)
    print(f"You have chosen the {player.character_class.name} class.")
else:
    print("Invalid choice.")

total_points = 5
while total_points > 0:
    init_add_stat_points(player, player.character_class, 1)
    total_points -= 1
    print(f"You have {total_points} points left.")

#playerstat
strength_point = player.character_class.strength.point
dexterity_point = player.character_class.dexterity.point
intelligence_point = player.character_class.intelligence.point
mind_point = player.character_class.mind.point
luck_point = player.character_class.luck.point
vitality_point = player.character_class.vitality.point

# Save character data
player.create(strength_point, dexterity_point, intelligence_point, mind_point, luck_point, vitality_point)


#create goblin enemy for test
goblin = Character("Goblin", 5, 1, 50, 30, 40, "Goblin", "Male")
goblin.character_class = swordman("Swordman", strength, dexterity, intelligence, mind, luck, vitality)
goblin.create(1, 1, 1, 1, 1, 1)
