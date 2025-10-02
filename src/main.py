from simulation import Simulation
from game_map import GameMap
from map_renderer import MapRenderer


def main():
    game_map = GameMap(10, 10)
    map_render = MapRenderer()
    simulation = Simulation(game_map, map_render)

    simulation.init()
    simulation.start()


if __name__ == "__main__":
    main()
