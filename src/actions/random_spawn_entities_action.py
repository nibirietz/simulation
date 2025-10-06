from actions import RandomSpawnAction
from entities import Grass, Herbivore, Predator
from game_map import GameMap

PREDATORS_SPAWN_RATE = 0.1
HERBIVORE_SPAWN_RATE = 0.15
GRASS_SPAWN_RATE = 0.15


class RandomSpawnEntitiesAction(RandomSpawnAction):
    @classmethod
    def execute(cls, game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        grasses_amount = int(GRASS_SPAWN_RATE * game_map_square ** 0.5)
        herbivores_amount = int(HERBIVORE_SPAWN_RATE * game_map_square ** 0.5)
        predators_amount = int(PREDATORS_SPAWN_RATE * game_map_square ** 0.5)

        grasses = cls._generate_random_entities(game_map, Grass, grasses_amount)
        herbivores = cls._generate_random_entities(game_map, Herbivore, herbivores_amount)
        predators = cls._generate_random_entities(game_map, Predator, predators_amount)
        game_map.put_objects(grasses + herbivores + predators)
