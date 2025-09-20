from abc import abstractmethod

from src.board import Board
from src.coordinates import Coordinates
from src.entities.entities import Entity


class Creature(Entity):
    def __init__(self, coordinates: Coordinates, speed: int, hp: float):
        super().__init__(coordinates)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, board: Board):
        pass
