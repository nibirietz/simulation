from src.coordinates import Coordinates
from src.entities import Entity


class Grass(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
