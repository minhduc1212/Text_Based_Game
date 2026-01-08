from src.character import *
from src.character_class import swordman
from src.statistic import *

def init_add_stat_points(stat, points):
    print("You have 5 points to add to your class stats.")
    print("What stats do you want to add points to?")
    print("1. Strength")
    print("2. Dexterity")
    print("3. Intelligence")
    print("4. Mind")
    print("5. Luck")
    print("6. Vitality")

    choice = input("Enter the number of your choice: ")
    if choice == "1":
        player.character_class.strength.add_point(1)
    elif choice == "2":
        player.character_class.dexterity.add_point(1)
    elif choice == "3":
        player.character_class.intelligence.add_point(1)
    elif choice == "4":
        player.character_class.mind.add_point(1)
    elif choice == "5":
        player.character_class.luck.add_point(1)
    elif choice == "6":
        player.character_class.vitality.add_point(1)



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
    init_add_stat_points(player.character_class, 1)
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
