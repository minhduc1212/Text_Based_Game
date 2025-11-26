from world.world import world 

class top(world):
    def __init__(self, climate, world_size, world_name):
        super().__init__(world_name, world_size)
        self.climate = climate
       