from abc import abstractmethod
import game_map
from src.coordinates import Coordinates
from src.entities.entity import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, hp: float):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp

    def get_damage(self, attack_power: float):
        self.hp -= attack_power

    def is_alive(self):
        return self.hp > 0
