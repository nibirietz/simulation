import game_map
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
                current_map.remove_object(self.coordinates)
                current_map.put_object(penultimate_coordinates, self)

            self.eat(current_map, path[-1])

    def eat(self, current_map: game_map.GameMap, target_coordinates: Coordinates):
        # TODO: переделать заглушку
        current_map.remove_object(target_coordinates)
        current_map.remove_object(self.coordinates)
        current_map.put_object(target_coordinates, self)
