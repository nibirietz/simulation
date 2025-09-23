from src.coordinates import Coordinates
from src.entities import Creature
import game_map


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1):
        super().__init__(coordinates, speed, hp)

    def make_move(self, current_map: game_map.GameMap, path: list[Coordinates]):
        pass
