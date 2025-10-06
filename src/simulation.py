import select
import sys
from time import sleep

from actions import Action, RandomSpawnEntitiesAction, MoveAllCreaturesAction, RandomSpawnImmutablesEntitiesAction
from game_map import GameMap
from map_renderer import MapRenderer


class Simulation:
    def __init__(self, game_map: GameMap, map_renderer: MapRenderer):
        self.game_map = game_map
        self.move_counter = 0
        self.map_renderer = map_renderer
        self.init_actions: list[Action] = [RandomSpawnImmutablesEntitiesAction(), RandomSpawnEntitiesAction(),
                                           RandomSpawnEntitiesAction()]
        self.turn_actions: list[Action] = [MoveAllCreaturesAction(), RandomSpawnEntitiesAction()]

    def _execute_actions(self, actions: list[Action]):
        for action in actions:
            action.execute(self.game_map)

    def init(self):
        self._execute_actions(self.init_actions)
        self.map_renderer.render(self.game_map, self.move_counter)

    def next_turn(self):
        self.move_counter += 1
        self._execute_actions(self.turn_actions)
        self.map_renderer.render(self.game_map, self.move_counter)

    def start(self):
        while True:
            self.next_turn()
            sleep(0.5)
            if self.map_renderer.is_pause():
                break
