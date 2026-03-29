from loguru import logger

from fake_map_renderer import FakeMapRenderer
from logs import start_logging
from map_renderer import MapRenderer
from simulation import Simulation
from game_map import GameMap


def main():
    game_map = GameMap(10, 10)
    map_render = MapRenderer()
    simulation = Simulation(game_map, map_render)

    simulation.init()
    start_logging()
    simulation.start()
    logger.info("Закрытие симуляции")


if __name__ == "__main__":
    main()
