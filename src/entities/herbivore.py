from src.coordinates import Coordinates
from src.entities.creature import Creature
from src.game_map import GameMap


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1):
        super().__init__(coordinates, speed, hp)

    def make_move(self, game_map: GameMap, new_coordinates: Coordinates):
        if new_coordinates not in game_map.neighbour_coordinates(self.coordinates): return
        if game_map.is_square_empty(new_coordinates):
            game_map.remove_object(self.coordinates)
            game_map.put_object(new_coordinates, self)
            return
