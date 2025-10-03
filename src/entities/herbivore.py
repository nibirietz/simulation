from coordinates import Coordinates
from entities import Creature


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 10, max_hp: float = 15):
        super().__init__(coordinates, speed, hp, max_hp)
