from config import PredatorConfig
from coordinates import Coordinates
from entities import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates,
                 speed: int = PredatorConfig.SPEED,
                 hp: float = PredatorConfig.HP,
                 attack_power: int = PredatorConfig.ATTACK_POWER,
                 max_hp: float = PredatorConfig.MAX_HP):
        super().__init__(coordinates, speed, hp, max_hp)
        self.attack_power = attack_power
