from src.coordinates import Coordinates
from src.entities.entities import Entity


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.coordinates = dict()

    def put_object(self, coordinates: Coordinates, entity: Entity):
        entity.coordinates = coordinates
        self.coordinates[coordinates] = entity
