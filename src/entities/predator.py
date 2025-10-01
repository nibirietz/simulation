import game_map
import src.entities
from src.coordinates import Coordinates
from src.entities import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        if path is None:
            return

        if self.speed + 1 >= len(path):
            if len(path) >= 2:
                penultimate_coordinates = path[-2]
                self.shift(current_map, penultimate_coordinates)

            self.eat(current_map, path[-1])
        else:
            self.shift(current_map, path[self.speed])

    def eat(self, current_map: game_map.GameMap, target_coordinates: Coordinates):
        if isinstance(current_map.get_object(target_coordinates), src.entities.Herbivore):
            current_map.remove_object(target_coordinates)
            self.shift(current_map, target_coordinates)
