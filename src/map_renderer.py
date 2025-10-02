import os
from entities import Herbivore, Predator, Grass
from game_map import GameMap
from coordinates import Coordinates


class MapRenderer:
    empty_cell = "🟥"
    predator = "🐺"
    herbivore = "🐇"
    grass = "☘️"

    def render(self, game_map: GameMap):
        os.system('clear')

        print("-------")
        for i in range(game_map.width):
            line = ""
            for j in range(game_map.height):
                coordinates = Coordinates(i, j)

                if game_map.is_cell_empty(coordinates):
                    line += f" {self.empty_cell} "
                else:
                    entity = game_map.get_object(coordinates)
                    match entity:
                        case Predator():
                            line += f" {self.predator} "
                        case Herbivore():
                            line += f" {self.herbivore} "
                        case Grass():
                            line += f" {self.grass} "
                        case _:
                            line += f" - "

            print(line)
        print("-------")
