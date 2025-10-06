from random import randrange
from typing import TypeVar, Type

from actions import Action
from coordinates import Coordinates
from entities import Entity, Grass, Herbivore, Predator
from game_map import GameMap

T = TypeVar("T", bound=Entity)

PREDATORS_SPAWN_RATE = 0.2
HERBIVORE_SPAWN_RATE = 0.3
GRASS_SPAWN_RATE = 0.3


class SpawnRandomEntitiesAction(Action):
    @staticmethod
    def execute(game_map: GameMap):
        game_map_square = game_map.width * game_map.height
        grasses_amount = GRASS_SPAWN_RATE * game_map_square ** 0.5
        herbivores_amount = HERBIVORE_SPAWN_RATE * game_map_square ** 0.5
        predators_amount = PREDATORS_SPAWN_RATE * game_map_square ** 0.5

        grasses = SpawnRandomEntitiesAction._generate_random_entities(game_map, Grass, grasses_amount)
        herbivores = SpawnRandomEntitiesAction._generate_random_entities(game_map, Herbivore, herbivores_amount)
        predators = SpawnRandomEntitiesAction._generate_random_entities(game_map, Predator, predators_amount)
        game_map.put_objects(grasses + herbivores + predators)

    @staticmethod
    def _generate_random_empty_coordinates(game_map: GameMap) -> Coordinates:
        coordinates = Coordinates(randrange(0, game_map.height), randrange(0, game_map.width))
        while not game_map.is_cell_empty(coordinates):
            coordinates = Coordinates(randrange(0, game_map.height), randrange(0, game_map.width))

        return coordinates

    @staticmethod
    def _generate_random_entities(game_map: GameMap, type_entity: Type[T], amount: int) -> list[Entity]:
        generated_entities: list[type_entity] = []

        for _ in range(amount):
            random_coordinates = SpawnRandomEntitiesAction._generate_random_empty_coordinates(game_map)
            generated_entities.append(type_entity(random_coordinates))

        return generated_entities
