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
