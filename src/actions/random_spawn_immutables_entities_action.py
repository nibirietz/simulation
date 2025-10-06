from actions.random_spawn_action import RandomSpawnAction
from entities import Rock
from game_map import GameMap


class RandomSpawnImmutablesEntitiesAction(RandomSpawnAction):
    @staticmethod
    def execute(game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        rocks_amount = int(0.3 * game_map_square ** 0.5)

        rocks = RandomSpawnImmutablesEntitiesAction._generate_random_entities(game_map, Rock, rocks_amount)
        game_map.put_objects(rocks)
