import os
import select
import sys

from entities import Herbivore, Predator, Grass, Rock, DeadCreature, Tree
from game_map import GameMap
from coordinates import Coordinates


class MapRenderer:
    empty_cell = "🟫"
    predator = "🐺"
    herbivore = "🐇"
    grass = "🌱"
    rock = "🪨"
    dead_creature = "🦴"
    tree = "🌳"

    def render(self, game_map: GameMap, move_counter: int):
        os.system("clear")

        print(f"Ходов сделано: {move_counter}.")
        for i in range(game_map.width):
            line = ""
            for j in range(game_map.height):
                coordinates = Coordinates(i, j)

                if game_map.is_cell_empty(coordinates):
                    line += f"{self.empty_cell}"
                else:
                    entity = game_map.get_object(coordinates)
                    match entity:
                        case Predator():
                            line += f"{self.predator}"
                        case Herbivore():
                            line += f"{self.herbivore}"
                        case Grass():
                            line += f"{self.grass}"
                        case Rock():
                            line += f"{self.rock}"
                        case DeadCreature():
                            line += f"{self.dead_creature}"
                        case Tree():
                            line += f"{self.tree}"
                        case _:
                            line += f"-"

            print(line)
        print("-" * game_map.width * 2)
        print("Чтобы остановить напишите p. Чтобы выйти напишите e.")

    def is_pause(self) -> bool:
        if sys.stdin in select.select([sys.stdin], [], [], 0.5)[0]:
            user_input = input().strip().lower()
            if user_input == "p":
                return True
        return False

    def is_exit(self) -> bool:
        if sys.stdin in select.select([sys.stdin], [], [], 0.5)[0]:
            user_input = input().strip().lower()
            if user_input == "e":
                return True
