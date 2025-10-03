from coordinates import Coordinates
from entities.entity import Entity
from abc import ABC


class Creature(Entity, ABC):
    def __init__(self, coordinates: Coordinates, speed: int, hp: float, max_hp: float):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp
        self.max_hp = max_hp

    def cause_damage(self, attack_power: float):
        self.hp -= attack_power

    def cure_hp(self, hp: float):
        self.hp += hp
        self.hp %= self.max_hp

    def is_alive(self):
        return self.hp > 0
