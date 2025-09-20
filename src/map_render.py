from src.game_map import GameMap
from src.coordinates import Coordinates
from src.entities.predator import Predator


class MapRender:
    empty_cell = "🟥"
    predator = "🐺"

    def render(self, board: GameMap):
        for i in range(board.width):
            line = ""
            for j in range(board.height):
                coordinates = Coordinates(i, j)

                if board.is_square_empty(coordinates):
                    line += f" {self.empty_cell} "
                else:
                    match type(board.get_object(coordinates)):
                        case Predator:
                            line += f" {self.predator} "

            print(line)
