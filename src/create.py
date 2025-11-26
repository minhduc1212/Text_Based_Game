import world.world as world
import world.top as top

world_instance = world.world("FantasyLand", "Large")
top_level = top.top("Cold", "Large", "FantasyLand")

print(f"World Name: {world_instance.world_name}, World Size: {world_instance.world_size}")
print("in the top level")
print(f"Climate: {top_level.climate}, World Name: {top_level.world_name}, World Size: {top_level.world_size}")