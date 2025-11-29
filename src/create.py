from world.continent import Continent
from world.world import World
import random

#create the world
world_size = random.randint(1000000, 100000000)
first_world = World("The Not", world_size, "Solar System", "The first world")

#percentage of oceans in the world
ocean_percentage = random.uniform(0.45, 0.7)

#random the percentage of continents in the world
sum_percentage = 0
list_continent_percentage = []
for continent in range (first_world.number_children):
    if sum_percentage >= 1:
        #del the last continent percentage (which made the sum > 1)
        del list_continent_percentage[-1]
        #re calculate the last continent percentage
        continent_percentage = 1 - sum_percentage
        list_continent_percentage.append(continent_percentage)
        break
    else:
        if continent == first_world.number_children - 1:
            continent_percentage = 1 - sum_percentage
        else:
            continent_percentage = random.uniform(0.1, 0.3)
            sum_percentage += continent_percentage
        list_continent_percentage.append(continent_percentage)


FIRST_CONTINENT = Continent("The Dark", 12742, "Equator", "The first continent")
first_world.add_children(FIRST_CONTINENT)
print(f"World: {first_world.name}, The First Continent: {first_world.children[0].name}")