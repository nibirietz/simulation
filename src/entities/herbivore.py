from src.coordinates import Coordinates
from src.entities.creature import Creature
from src.game_map import GameMap


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1):
        super().__init__(coordinates, speed, hp)

    def make_move(self, game_map: GameMap, new_coordinates: Coordinates):
        self.go_to_cell(game_map, new_coordinates)
