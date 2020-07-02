class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:

        if len(coordinates) < 2:
            return -1

        if len(coordinates) == 2:
            return True

        for i in range(1, len(coordinates) - 1):
            if coordinates[i][1] == coordinates[i - 1][1] or coordinates[i][0] == coordinates[i - 1][0]:
                continue
            elif (coordinates[i][0] - coordinates[i - 1][0]) / (coordinates[i][1] - coordinates[i - 1][1]) != (
                    coordinates[i + 1][0] - coordinates[i][0]) / (coordinates[i + 1][1] - coordinates[i][1]):

                return False

        return True

