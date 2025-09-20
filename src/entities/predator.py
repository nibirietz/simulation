from src.board import Board
from src.coordinates import Coordinates
from src.entities.creature import Creature


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int = 1, hp: float = 1, attack_power: int = 1):
        super().__init__(coordinates, speed, hp)
        self.attack_power = attack_power

    def make_move(self, board: Board):
        pass

    def attack_herbivore(self):
        pass
