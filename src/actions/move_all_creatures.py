from actions import Action
from controllers import CreatureMover
from coordinates import Coordinates
from entities import Entity, Predator, Herbivore, Grass, Creature
from game_map import GameMap


class MoveAllCreatures(Action):
    @staticmethod
    def execute(game_map: GameMap):
        creatures = [entity for entity in game_map.get_entities() if isinstance(entity, Creature)]
        for creature in creatures:
            CreatureMover.make_move(game_map, creature, MoveAllCreatures._get_targets(game_map, creature))

    @staticmethod
    def _get_targets(game_map: GameMap, entity: Entity) -> list[Coordinates]:
        if isinstance(entity, Predator):
            return [entity.coordinates for entity in game_map.get_entities() if isinstance(entity, Herbivore)]
        if isinstance(entity, Herbivore):
            return [entity.coordinates for entity in game_map.get_entities() if isinstance(entity, Grass)]
