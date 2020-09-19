# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
#
#
# Example 1:
#
# Input: "GGLLGG"
# Output: true
# Explanation:
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.


# It is an interesting question, we need to know a rule that in two situation, if will has circle
# 1. The face direction after one loop must different from the ordinal direction
# 2. If not, need to back to start point after one loop
# So we just need to prove that 2 conditions
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Use a number to indicate the direction
        # North = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position and direction
        x,y = 0,0
        direct = 0

        for i in instructions:
            if i == "L":
                direct = (direct + 3) % 4
            elif i == "R":
                direct = (direct + 1) % 4
            else:
                x += directions[direct][0]
                y += directions[direct][1]

            # after one cycle:
            # robot returns into initial position
            # or robot doesn't face north
            return (x == 0 and y == 0) or direct != 0

