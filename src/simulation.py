from time import sleep

from actions import Actions
from game_map import GameMap
from map_renderer import MapRenderer


class Simulation:
    def __init__(self, game_map: GameMap, map_renderer: MapRenderer, actions: Actions):
        self.game_map = game_map
        self.move_counter = 0
        self.map_renderer = map_renderer
        self.actions = actions

    def init(self):
        self.actions.init_actions(self.game_map)

    def next_turn(self):
        self.move_counter += 1
        self.actions.turn_actions(self.game_map)
        self.map_renderer.render(self.game_map)

    def start(self):
        while True:
            self.next_turn()
            sleep(0.5)
