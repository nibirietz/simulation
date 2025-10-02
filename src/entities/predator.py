import game_map
import src.entities
from src.coordinates import Coordinates
from src.entities import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 10, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        self.get_damage(current_map, 1)
        if path is None or not self.is_alive():
            return

        if self.speed + 1 >= len(path):
            if len(path) >= 2:
                penultimate_coordinates = path[-2]
                self.shift(current_map, penultimate_coordinates)
            self.eat(current_map, path[-1])
        else:
            self.shift(current_map, path[self.speed])

    def eat(self, current_map: game_map.GameMap, target_coordinates: Coordinates):
        if current_map.is_cell_empty(target_coordinates):
            return
        enemy = current_map.get_object(target_coordinates)
        if isinstance(enemy, src.entities.Herbivore):
            enemy.get_damage(current_map, self.attack_power)
            self.hp += 5
            self.shift(current_map, target_coordinates)
