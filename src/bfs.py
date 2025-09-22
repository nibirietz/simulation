from collections import deque

from src.coordinates import Coordinates
from src.entities.entities import Entity
from src.entities.herbivore import Herbivore
from src.entities.predator import Predator
from src.game_map import GameMap


class BFS:
    # @staticmethod
    # def minimal_path(paths: list[list[Coordinates]]) -> list[Coordinates] | None:
    #     if len(paths) == 0: return None
    #     result = paths[0]
    #
    #     for path in paths:
    #         if len(path) < len(result):
    #             result = path
    #
    #     return result

    @staticmethod
    def search_path(game_map: GameMap, start_coordinates: Coordinates, targets: list[Coordinates]) -> list[
                                                                                                          Coordinates] | None:
        queue = deque([start_coordinates])
        previous_cell = {start_coordinates: None}
        # paths = []

        while queue:
            current_coordinates = queue.popleft()

            if current_coordinates in targets:
                path = []
                path_point = current_coordinates

                while path_point is not None:
                    path.append(path_point)
                    path_point = previous_cell[path_point]

                path.reverse()
                # paths.append(path)
                return path

            for neighbour in game_map.neighbour_coordinates(current_coordinates):
                if neighbour in previous_cell:
                    continue

                if game_map.is_square_empty(neighbour) or neighbour in targets:
                    previous_cell[neighbour] = current_coordinates
                    queue.append(neighbour)

        return None
