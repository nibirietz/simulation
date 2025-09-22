class Coordinates:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def __add__(self, other):
        return Coordinates(self.row + other.row, self.column + other.column)

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.row, self.column))
