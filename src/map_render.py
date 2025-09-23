from src.entities import Herbivore, Predator
from src.game_map import GameMap
from src.coordinates import Coordinates


class MapRender:
    empty_cell = "🟥"
    predator = "🐺"
    herbivore = "🐇"

    def render(self, board: GameMap):
        for i in range(board.width):
            line = ""
            for j in range(board.height):
                coordinates = Coordinates(i, j)

                if board.is_cell_empty(coordinates):
                    line += f" {self.empty_cell} "
                else:
                    entity = board.get_object(coordinates)
                    match entity:
                        case Predator():
                            line += f" {self.predator} "
                        case Herbivore():
                            line += f" {self.herbivore} "
                        case _:
                            line += f" - "

            print(line)
