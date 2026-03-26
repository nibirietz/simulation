from abc import abstractmethod
from random import randrange
from typing import TypeVar, Type

from actions import Action
from coordinates import Coordinates
from entities import Entity
from game_map import GameMap

T = TypeVar("T", bound=Entity)


class SpawnAction(Action):
    @abstractmethod
    def execute(self, game_map: GameMap):
        pass

    def _generate_random_empty_coordinates(self, game_map: GameMap) -> Coordinates:
        coordinates = Coordinates(randrange(0, game_map.height), randrange(0, game_map.width))
        while not game_map.is_cell_empty(coordinates):
            coordinates = Coordinates(randrange(0, game_map.height), randrange(0, game_map.width))

        return coordinates

    def _generate_random_entities(self, game_map: GameMap, type_entity: Type[T], amount: int) -> list[Entity]:
        generated_entities: list = []

        for _ in range(amount):
            random_coordinates = self._generate_random_empty_coordinates(game_map)
            generated_entities.append(type_entity(random_coordinates))

        return generated_entities
