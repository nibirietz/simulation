from abc import abstractmethod

from pychess.Utils.Board import Board

from src.game_map import GameMap
from src.coordinates import Coordinates
from src.entities.entities import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, hp: float):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, game_map: GameMap, new_coordinates: Coordinates):
        pass
