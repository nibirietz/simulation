from src.entities.herbivore import Herbivore
from src.game_map import GameMap
from src.map_render import MapRender
from src.coordinates import Coordinates
from src.entities.predator import Predator
from src.bfs import BFS


def main():
    game_map = GameMap(10, 10)
    entity = Predator(Coordinates(1, 1))
    game_map.put_object(Coordinates(1, 1), entity)
    entity.make_move(game_map, Coordinates(1, 2))
    entity2 = Herbivore(Coordinates(1, 4))
    game_map.put_object(Coordinates(1, 4), entity2)
    entity3 = Herbivore(Coordinates(3, 1))
    game_map.put_object(Coordinates(3, 1), entity3)
    entity4 = Herbivore(Coordinates(0, 1))
    game_map.put_object(Coordinates(0, 1), entity4)

    map_render = MapRender()
    map_render.render(game_map)
    bfs = BFS()
    print([(coordinates.row, coordinates.column) for coordinates in
           bfs.search_path(game_map, entity.coordinates,
                           [entity2.coordinates, entity3.coordinates, entity4.coordinates])])


if __name__ == "__main__":
    main()
