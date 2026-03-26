from abc import ABC, abstractmethod

from game_map import GameMap


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: GameMap):
        pass
