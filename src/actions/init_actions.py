from random import randrange

from action import Action
from coordinates import Coordinates
from game_map import GameMap


class InitActions(Action):
    @staticmethod
    def generate_random_coordinates(game_map: GameMap) -> Coordinates:
        return Coordinates(randrange(0, game_map.height), randrange(0, game_map.width))

    @staticmethod
    def execute(game_map: GameMap):
        pass
