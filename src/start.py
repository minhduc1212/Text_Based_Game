def init_add_stat_points(player, stat, points):
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