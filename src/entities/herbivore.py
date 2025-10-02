import src.entities
from src.coordinates import Coordinates
from src.entities import Creature
import game_map


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 10):
        super().__init__(coordinates, speed, hp)

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        self.get_damage(current_map, 1)

        if path is None or not self.is_alive():
            return

        if self.speed + 1 >= len(path):
            self.eat(current_map, path[-1])
        else:
            self.hp -= 1
            self.shift(current_map, path[self.speed])

    def eat(self, current_map: game_map.GameMap, target_coordinates: Coordinates):
        if current_map.is_cell_empty(target_coordinates):
            return
        if isinstance(current_map.get_object(target_coordinates), src.entities.Grass):
            current_map.remove_object(target_coordinates)
            self.hp += 5
            self.shift(current_map, target_coordinates)
