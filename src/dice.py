import random
def roll_dice(number_of_sides: int, number_of_dice: int):
    total_point_dice = 0
    for _ in range(number_of_dice):
        point_dice = random.randint(1, number_of_sides)
        total_point_dice += point_dice
        
    return total_point_dice