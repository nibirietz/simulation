from actions import SpawnAction
from config import SpawnConfig
from entities import Grass, Herbivore, Predator
from game_map import GameMap


class DynamicSpawnAction(SpawnAction):
    def execute(self, game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        grasses_amount = int(SpawnConfig.GRASS_SPAWN_RATE * game_map_square ** 0.5)
        herbivores_amount = int(SpawnConfig.HERBIVORE_SPAWN_RATE * game_map_square ** 0.5)
        predators_amount = int(SpawnConfig.PREDATORS_SPAWN_RATE * game_map_square ** 0.5)

        if len(game_map.objects) < 0.7 * game_map_square:
            grass_count = list(grass for grass in game_map.objects if isinstance(grass, Grass))
            grasses = []
            if len(grass_count) < 0.2 * game_map_square:
                grasses = self._generate_random_entities(game_map, Grass, grasses_amount)

            herbivores = self._generate_random_entities(game_map, Herbivore, herbivores_amount)
            predators = self._generate_random_entities(game_map, Predator, predators_amount)
            game_map.put_objects(grasses + herbivores + predators)
