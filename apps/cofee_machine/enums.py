from enum import Enum


class Strength(Enum):
    """
    Enumeration for coffee strength levels.

    This enumeration defines different strength levels for coffee. Each strength level is represented by a
    unique constant value.

    Constants:
        NORMAL (int): Normal coffee strength level.
        STRONG (int): Strong coffee strength level.
        EXTRA_STRONG (int): Extra strong coffee strength level.
    """

    NORMAL = 1
    STRONG = 2
    EXTRA_STRONG = 3
