from src.coordinates import Coordinates
from src.entities import Creature
import game_map


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1):
        super().__init__(coordinates, speed, hp)

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        if path is None:
            return

        if self.speed + 1 >= len(path):
            self.eat(current_map, path[-1])
        else:
            self.shift(current_map, path[self.speed])

    def eat(self, current_map: game_map.GameMap, target_coordinates: Coordinates):
        current_map.remove_object(target_coordinates)
        self.shift(current_map, target_coordinates)
