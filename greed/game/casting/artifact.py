import random
from game.casting.actor import Actor

class Artifact(Actor):
    """Spawner is responsible for creating actors and 
        selecting starting positons."""

    def __init__(self):
        super.__init__()
        self._value = 0

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value





    # def create_actors(self):
    #     actor_count = random.randint(1, 5)
    #     for i in actor_count:
    #         self._actors.append()

    
    # def randomize_start_positions(self):
    #     pass