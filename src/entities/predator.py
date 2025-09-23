import game_map
from src.coordinates import Coordinates
from src.entities import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power

    # @staticmethod
    # def is_enemy_square(game_map: GameMap, coordinates: Coordinates):
    #     return type(game_map.get_object(coordinates)) == Herbivore

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        pass

    def attack(self, coordinates: Coordinates):
        pass
