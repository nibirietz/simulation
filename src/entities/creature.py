from abc import abstractmethod
import game_map
from src.coordinates import Coordinates
from src.entities.entity import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, hp: float):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        pass

    def shift(self, current_map: game_map.GameMap, new_coordinates: Coordinates):
        if current_map.is_cell_empty(new_coordinates):
            current_map.remove_object(self.coordinates)
            current_map.put_object(new_coordinates, self)
            self.coordinates = new_coordinates

    def get_damage(self, current_map: game_map.GameMap, attack_power: float):
        self.hp -= attack_power
        if self.hp <= 0:
            current_map.remove_object(self.coordinates)

    def is_alive(self):
        return self.hp > 0
