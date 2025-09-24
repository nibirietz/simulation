from coordinates import Coordinates
from src.entities.grass import Grass
from src.breadfirstsearch import BreadFirstSearch
from src.entities import Creature, Herbivore, Predator
from src.game_map import GameMap


class Actions:
    @staticmethod
    def init_actions(game_map: GameMap):
        game_map.put_objects(
            [
                Herbivore(Coordinates(1, 1)),
                Herbivore(Coordinates(2, 4)),
                Predator(Coordinates(3, 7)),
                Predator(Coordinates(4, 2)),
                Grass(Coordinates(0, 4)),
            ]
        )

    @staticmethod
    def turn_actions(game_map: GameMap) -> GameMap:
        creatures = [creature for creature in game_map.get_entities() if isinstance(creature, Creature)]
        herbivores = [herbivore for herbivore in creatures if isinstance(herbivore, Herbivore)]
        predators = [predator for predator in creatures if isinstance(predator, Predator)]
        herbivores_coordinates = [herbivore.coordinates for herbivore in herbivores]
        grasses_coordinates = [grass.coordinates for grass in game_map.get_entities() if isinstance(grass, Grass)]

        bfs = BreadFirstSearch()

        for herbivore in herbivores:
            path = bfs.search_path(game_map, herbivore.coordinates, grasses_coordinates)
            herbivore.make_move(game_map, path)

        for predator in predators:
            path = bfs.search_path(game_map, predator.coordinates, herbivores_coordinates)
            predator.make_move(game_map, path)

        return game_map
