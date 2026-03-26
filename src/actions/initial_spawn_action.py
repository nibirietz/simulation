from actions import SpawnAction
from config import SpawnConfig
from entities import Rock, Tree
from game_map import GameMap


class InitialSpawnAction(SpawnAction):
    def execute(self, game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        rocks_amount = int(SpawnConfig.ROCKS_SPAWN_RATE * game_map_square ** 0.5)
        trees_amount = int(SpawnConfig.TREES_SPAWN_RATE * game_map_square ** 0.5)

        rocks = self._generate_random_entities(game_map, Rock, rocks_amount)
        trees = self._generate_random_entities(game_map, Tree, trees_amount)
        game_map.put_objects(rocks + trees)
