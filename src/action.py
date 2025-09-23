from src.breadfirstsearch import BreadFirstSearch
from src.entities import Creature, Herbivore, Predator
from src.game_map import GameMap


class Action:
    @staticmethod
    def init_actions(game_map: GameMap):
        pass

    @staticmethod
    def turn_actions(game_map: GameMap):
        creatures = [creature for creature in game_map.get_entities() if isinstance(creature, Creature)]
        herbivores = [herbivore for herbivore in creatures if isinstance(herbivore, Herbivore)]
        predators = [predator for predator in creatures if isinstance(predator, Predator)]
        herbivores_coordinates = [herbivore.coordinates for herbivore in herbivores]

        for predator in predators:
            bfs = BreadFirstSearch()
            path = bfs.search_path(game_map, predator.coordinates, herbivores_coordinates)
            predator.make_move(game_map, path)
