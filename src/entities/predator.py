from coordinates import Coordinates
from entities import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 10, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power
