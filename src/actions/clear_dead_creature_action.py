from actions import Action
from entities import DeadCreature
from game_map import GameMap


class ClearDeadCreatureAction(Action):
    @staticmethod
    def execute(game_map: GameMap):
        dead_creatures = [entity for entity in game_map.get_entities() if isinstance(entity, DeadCreature)]
        for dead_creature in dead_creatures:
            game_map.remove_object(dead_creature.coordinates)
