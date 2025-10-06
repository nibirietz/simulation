from abc import ABC, abstractmethod

from game_map import GameMap


class Action(ABC):
    @staticmethod
    @abstractmethod
    def execute(game_map: GameMap):
        pass
