from src.coordinates import Coordinates
from src.entities import Creature


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 10):
        super().__init__(coordinates, speed, hp)
