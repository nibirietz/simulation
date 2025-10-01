from time import sleep

from actions import Actions
from entities import Grass
from game_map import GameMap
from map_renderer import MapRenderer


class Simulation:
    def __init__(self, game_map: GameMap, map_renderer: MapRenderer):
        self.game_map = game_map
        self.move_counter = 0
        self.map_renderer = map_renderer
        self.actions = Actions(game_map)

    def init(self):
        self.actions.init()
        self.map_renderer.render(self.game_map)

    def next_turn(self):
        self.move_counter += 1
        self.game_map.put_objects(self.actions.generate_random_entities(Grass, 0.3))
        self.actions.turn_actions()
        self.map_renderer.render(self.game_map)

    def start(self):
        while True:
            self.next_turn()
            sleep(0.5)
