from simulation import Simulation
from src.actions import Actions
from src.game_map import GameMap
from src.map_renderer import MapRenderer


def main():
    game_map = GameMap(10, 10)
    map_render = MapRenderer()
    actions = Actions()
    simulation = Simulation(game_map, map_render, actions)

    simulation.init()
    print(game_map.get_entities())
    simulation.start()


if __name__ == "__main__":
    main()
