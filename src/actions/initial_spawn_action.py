from actions import SpawnAction
from entities import Rock
from game_map import GameMap

ROCKS_SPAWN_RATE = 0.3


class InitialSpawnAction(SpawnAction):
    @classmethod
    def execute(cls, game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        rocks_amount = int(ROCKS_SPAWN_RATE * game_map_square ** 0.5)

        rocks = cls._generate_random_entities(game_map, Rock, rocks_amount)
        game_map.put_objects(rocks)
