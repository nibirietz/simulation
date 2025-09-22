from abc import ABC

from src.coordinates import Coordinates


class Entity(ABC):
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
