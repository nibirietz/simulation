from src.entities.entity import Entity
from src.coordinates import Coordinates


class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.objects: dict[Coordinates, Entity] = dict()

    def put_object(self, coordinates: Coordinates, entity: Entity):
        self.objects[coordinates] = entity

    def put_objects(self, entities: list[Entity]):
        for entity in entities:
            self.put_object(entity.coordinates, entity)

    def get_object(self, coordinates: Coordinates) -> Entity:
        return self.objects[coordinates]

    def remove_object(self, coordinates: Coordinates):
        del self.objects[coordinates]

    def is_cell_empty(self, coordinates: Coordinates) -> Entity:
        return coordinates not in self.objects

    def is_valid_coordinates(self, coordinates: Coordinates):
        if coordinates.row < 0 or coordinates.row > self.width: return False
        if coordinates.column < 0 or coordinates.column > self.height: return False
        return True

    def neighbour_coordinates(self, coordinates: Coordinates):
        neighbours = [
            coordinates + Coordinates(0, -1), coordinates + Coordinates(-1, 0),
            coordinates + Coordinates(1, 0), coordinates + Coordinates(0, 1)
        ]

        return [coordinates for coordinates in neighbours if self.is_valid_coordinates(coordinates)]

    def get_entities(self) -> list[Entity]:
        return list(self.objects.values())
