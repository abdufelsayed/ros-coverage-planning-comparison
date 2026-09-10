"""Grid headings shared by spiral and backtracking."""

import enum

class Direction(enum.Enum):
    east = -1
    south = 0
    west = 1
    north = 2

    def left(self):
        value = self.value
        if value == -1:
            return Direction(2)
        else:
            return Direction(value - 1)

    def right(self):
        value = self.value
        if value == 2:
            return Direction(-1)
        else:
            return Direction(value + 1)
