from game.casting.actor import Actor

class Character(Actor):
    """tracks the characters score."""

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """returns the score as an Int."""
        return self._score

    def set_score(self, score):
        """sets the characters score.
            score (Int)"""
        self._score = score