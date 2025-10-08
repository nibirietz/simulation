from coordinates import Coordinates
from entities import Entity


class DeadCreature(Entity):
    def __init__(self, coordinates: Coordinates):
        super().__init__(coordinates)
