from collections import deque

from src.coordinates import Coordinates
from src.game_map import GameMap


class BreadFirstSearch:
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

                if game_map.is_cell_empty(neighbour) or neighbour in targets:
                    previous_cell[neighbour] = current_coordinates
                    queue.append(neighbour)

        return None
