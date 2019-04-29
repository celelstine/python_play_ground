"""play with Enum"""

from enum import Enum


class Temperament(Enum):
    """list of temperaments in human with a description"""

    sanguine = "impulsive and pleasure-seeking"
    choleric = "ambitious and leader-like"
    phlegmatic = "relaxed and quiet"
    melancholic = "introverted and thoughtful"


for temp in Temperament:
    print("{}: {}".format(temp.name, temp.value))