from actions import Action
from breadfirstsearch import BreadFirstSearch
from controllers import CreatureController
from coordinates import Coordinates
from entities import Entity, Predator, Herbivore, Grass, Creature
from game_map import GameMap


class MoveAllCreaturesAction(Action):
    @staticmethod
    def execute(game_map: GameMap):
        creatures = [entity for entity in game_map.get_entities() if isinstance(entity, Creature)]

        bfs = BreadFirstSearch()
        for creature in creatures:
            targets = MoveAllCreaturesAction._get_targets(game_map, creature)
            path = bfs.search_path(game_map, creature.coordinates, targets)
            CreatureController.make_move(game_map, creature, path)

    @staticmethod
    def _get_targets(game_map: GameMap, entity: Entity) -> list[Coordinates]:
        if isinstance(entity, Predator):
            return [entity.coordinates for entity in game_map.get_entities() if isinstance(entity, Herbivore)]
        if isinstance(entity, Herbivore):
            return [entity.coordinates for entity in game_map.get_entities() if isinstance(entity, Grass)]
