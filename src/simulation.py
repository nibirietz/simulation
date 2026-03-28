from time import sleep

from actions import Action, DynamicSpawnAction, MoveAllCreaturesAction, InitialSpawnAction, ClearDeadCreaturesAction
from fake_map_renderer import FakeMapRenderer
from game_map import GameMap
from map_renderer import MapRenderer
from loguru import logger


class Simulation:
    def __init__(self, game_map: GameMap, map_renderer: MapRenderer | FakeMapRenderer):
        self.game_map = game_map
        self.move_counter = 0
        self.map_renderer = map_renderer
        self.init_actions: list[Action] = [InitialSpawnAction(), DynamicSpawnAction(),
                                           DynamicSpawnAction()]
        self.turn_actions: list[Action] = [ClearDeadCreaturesAction(), MoveAllCreaturesAction(), DynamicSpawnAction()]

    def _execute_actions(self, actions: list[Action]):
        for action in actions:
            action.execute(self.game_map)

    def init(self):
        self._execute_actions(self.init_actions)
        self.map_renderer.render(self.game_map, self.move_counter)
        logger.info("Запуск симуляции")

    def next_turn(self):
        self.move_counter += 1
        self._execute_actions(self.turn_actions)
        self.map_renderer.render(self.game_map, self.move_counter)
        logger.info(f"Ход номер: {self.move_counter}")

    def pause(self):
        while not self.map_renderer.is_pause():
            continue

    def start(self):
        while True:
            self.next_turn()
            # sleep(0.25)
            if self.map_renderer.is_pause():
                self.pause()
            if self.map_renderer.is_exit():
                break
            if self.move_counter == 1000:
                break
