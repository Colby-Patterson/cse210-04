from game.shared.color import Color
from game.shared.point import Point

class Actor:
    """The moving pieces to this game. It keeps track of it's
        text, size, position, speed, and color. It can also 
        set those variables to different values.
    
    Attributes:
        _text: the symbol that represents the piece on screen.
        _size: how large the symbol is.
        _position: where it is on the screen.
        _speed: the distance the actor will move.
        _color: the color of the piece.
    """

    def __init__(self):
        """See class docstring."""
        self._text = ""
        self._size = 1
        self._position = Point(0, 0)
        self._speed = Point(0, 0)
        self._color = Color(255, 255, 255)
        self._axis = 0

    def get_text(self):
        """Returns the actors text as a string."""
        return self._text

    def get_size(self):
        """Returns the actors size as an int."""
        return self._size

    def get_position(self):
        """Returns the actors position as a tuple with two ints."""
        return self._position

    def get_speed(self):
        """Returns the actors speed as a tuple with two ints."""
        return self._speed

    def get_color(self):
        """Returns the actors color as a tuple with three ints."""
        return self._color

    def get_axis(self):
        """Returns the actors axis as an int."""
        return self._axis

    def set_text(self, text):
        """Sets the actors text.
        text (String)"""
        self._text = text

    def set_size(self, size):
        """Sets the actors size.
        size (Int)"""
        self._size = size

    def set_position(self, position):
        """Sets the actors position.
        position (Int, Int)"""
        self._position = position

    def set_speed(self, speed):
        """Sets the actors speed.
        speed (Int)"""
        self._speed = speed

    def set_color(self, color):
        """Sets the actors color.
        color (Int, Int, Int)"""
        self._color = color

    def set_axis(self, axis):
        """Sets the actors axis.
        axis (Int)"""
        self._axis = axis
