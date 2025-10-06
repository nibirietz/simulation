from random import choice
from coordinates import Coordinates
from entities import Creature, Predator, Herbivore, Grass
from game_map import GameMap


class CreatureMover:
    @staticmethod
    def move_to_coordinates(game_map: GameMap, creature: Creature, coordinates: Coordinates):
        if game_map.is_cell_empty(coordinates):
            game_map.remove_object(creature.coordinates)
            game_map.put_object(coordinates, creature)
            creature.coordinates = coordinates

    @staticmethod
    def make_move(game_map: GameMap, creature: Creature, path: list[Coordinates]):
        creature.cause_damage(1)

        if not creature.is_alive():
            game_map.remove_object(creature.coordinates)
            return

        if path is None:
            CreatureMover.random_move(game_map, creature)
            return

        if creature.speed + 1 >= len(path):
            if len(path) >= 2:
                penultimate_coordinates = path[-2]
                CreatureMover.move_to_coordinates(game_map, creature, penultimate_coordinates)
            CreatureMover.eat(game_map, creature, path[-1])
        else:
            CreatureMover.move_to_coordinates(game_map, creature, path[creature.speed])

    @staticmethod
    def eat(game_map: GameMap, creature: Creature, coordinates: Coordinates):
        if game_map.is_cell_empty(coordinates):
            return

        enemy = game_map.get_object(coordinates)

        if isinstance(creature, Predator) and isinstance(enemy, Herbivore):
            enemy.cause_damage(creature.attack_power)
            creature.cure_hp(5)
            if not enemy.is_alive():
                game_map.remove_object(coordinates)
                CreatureMover.move_to_coordinates(game_map, creature, coordinates)

        if isinstance(creature, Herbivore) and isinstance(enemy, Grass):
            creature.cure_hp(5)
            game_map.remove_object(coordinates)
            CreatureMover.move_to_coordinates(game_map, creature, coordinates)

    @staticmethod
    def random_move(game_map: GameMap, creature: Creature):
        neighbours = [neighbour for neighbour in game_map.neighbour_coordinates(creature.coordinates) if
                      game_map.is_cell_empty(neighbour)]
        if neighbours:
            CreatureMover.move_to_coordinates(game_map, creature, choice(neighbours))
