from src.game_map import GameMap
from src.coordinates import Coordinates
from src.entities.creature import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power

    # @staticmethod
    # def is_enemy_square(game_map: GameMap, coordinates: Coordinates):
    #     return type(game_map.get_object(coordinates)) == Herbivore

    def make_move(self, game_map: GameMap, new_coordinates: Coordinates):
        if new_coordinates in game_map.neighbour_coordinates(self.coordinates) and game_map.is_square_empty(
                new_coordinates):
            self.go_to_cell(game_map, new_coordinates)

    def attack(self, coordinates: Coordinates):
        pass
