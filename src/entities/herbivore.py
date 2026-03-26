from config import HerbivoreConfig
from coordinates import Coordinates
from entities import Creature


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates,
                 speed: int = HerbivoreConfig.SPEED,
                 hp: float = HerbivoreConfig.HP,
                 max_hp: float = HerbivoreConfig.MAX_HP):
        super().__init__(coordinates, speed, hp, max_hp)
