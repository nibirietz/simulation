from src.action import Action
from src.entities import Entity, Creature, Predator, Herbivore
from src.game_map import GameMap
from src.map_render import MapRender
from src.coordinates import Coordinates
from src.breadfirstsearch import BreadFirstSearch


def main():
    game_map = GameMap(10, 10)
    entity1 = Predator(Coordinates(1, 1))
    print(isinstance(entity1, Entity))
    game_map.put_object(Coordinates(1, 1), entity1)
    entity2 = Herbivore(Coordinates(1, 4))
    game_map.put_object(Coordinates(1, 4), entity2)
    entity3 = Herbivore(Coordinates(3, 1))
    game_map.put_object(Coordinates(3, 1), entity3)
    entity4 = Herbivore(Coordinates(0, 1))
    game_map.put_object(Coordinates(0, 1), entity4)
    entity5 = Predator(Coordinates(8, 8))
    game_map.put_object(Coordinates(8, 8), entity5)
    actions = Action()
    actions.turn_actions(game_map)

    map_render = MapRender()
    map_render.render(game_map)
    # bfs = BreadFirstSearch()
    # print([(coordinates.row, coordinates.column) for coordinates in
    #        bfs.search_path(game_map, entity1.coordinates,
    #                        [entity2.coordinates, entity3.coordinates, entity4.coordinates])])


if __name__ == "__main__":
    main()
