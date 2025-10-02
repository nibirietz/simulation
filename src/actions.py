from random import randrange
from typing import Type

from typing_extensions import TypeVar

from coordinates import Coordinates
from controllers.creature_mover import CreatureMover
from breadfirstsearch import BreadFirstSearch
from entities import Creature, Herbivore, Predator, Entity, Grass
from game_map import GameMap

T = TypeVar("T", bound=Entity)


class Actions:
    def __init__(self, game_map: GameMap):
        self.game_map = game_map

    def init(self):
        # self.game_map.put_objects(
        #     [
        #         Herbivore(Coordinates(1, 1)),
        #         Herbivore(Coordinates(1, 3)),
        #         Grass(Coordinates(1, 2))
        #     ]
        # )
        # self.game_map.put_objects(self.generate_random_entities())
        herbivores = self.generate_random_entities(Herbivore, 0.69)
        predators = self.generate_random_entities(Predator, 0.33)
        grass = self.generate_random_entities(Grass, 0.7)

        self.game_map.put_objects(herbivores + predators + grass)

    def generate_random_coordinates(self) -> Coordinates:
        return Coordinates(randrange(0, self.game_map.height), randrange(0, self.game_map.width))

    def generate_random_entities(self, type_entity: Type[T], distribution_coefficient: float) -> list[Entity]:
        amount = int((self.game_map.width * self.game_map.height) ** distribution_coefficient)
        generated_entities: list[Entity] = []

        for i in range(amount):
            random_coordinates = self.generate_random_coordinates()
            if self.game_map.is_cell_empty(random_coordinates):
                generated_entities.append(type_entity(random_coordinates))

        return generated_entities

    def turn_actions(self):
        creatures = [creature for creature in self.game_map.get_entities() if isinstance(creature, Creature)]
        herbivores = [herbivore for herbivore in creatures if isinstance(herbivore, Herbivore)]
        predators = [predator for predator in creatures if isinstance(predator, Predator)]
        grasses_coordinates = [grass.coordinates for grass in self.game_map.get_entities() if isinstance(grass, Grass)]

        bfs = BreadFirstSearch()

        for herbivore in herbivores:
            path = bfs.search_path(self.game_map, herbivore.coordinates, grasses_coordinates)
            CreatureMover.make_move(self.game_map, herbivore, path)

        herbivores_coordinates = [herbivore.coordinates for herbivore in herbivores]

        for predator in predators:
            path = bfs.search_path(self.game_map, predator.coordinates, herbivores_coordinates)
            CreatureMover.make_move(self.game_map, predator, path)

        grass_count = len([grass for grass in self.game_map.get_entities() if isinstance(grass, Grass)])
        if grass_count < 5:
            grass = self.generate_random_entities(Grass, 0.3)
            self.game_map.put_objects(grass)
