import random
from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):
    """Spawner is responsible for creating actors and 
        selecting starting positons."""

    def __init__(self):
        super(Artifact, self).__init__()
        self._value = 0

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def change_position(self, max_x, max_y):
        """Changes the position of the actor based on the speed
            and the actors axis."""
        #self._position[self._axis] = self._position[self._axis] + self._speed
        x = self._position.get_x()
        y = (self._position.get_y() + self._speed.get_y()) % max_x
        self._position = Point(x, y)



    # def create_actors(self):
    #     actor_count = random.randint(1, 5)
    #     for i in actor_count:
    #         self._actors.append()

    
    # def randomize_start_positions(self):
    #     pass