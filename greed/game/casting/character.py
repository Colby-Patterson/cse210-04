from game.casting.actor import Actor
from game.shared.point import Point

class Character(Actor):
    """tracks the characters score."""

    def __init__(self):
        super(Character, self).__init__()
        self._score = 0

    def get_score(self):
        """returns the score as an Int."""
        return self._score

    def set_score(self, score):
        """sets the characters score.
            score (Int)"""
        self._score = score

    def change_position(self, max_x, max_y):
        """Changes the position of the actor based on the speed
            and the actors axis."""
        #self._position[self._axis] = self._position[self._axis] + self._speed
        x = (self._position.get_x() + self._speed.get_x()) % max_x
        y = max_y - 15
        self._position = Point(x, y)