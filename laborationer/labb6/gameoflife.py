#                     Conway's Game of Life
#                  --------------------------
#
# Original version by Guillaume Brunerie, adapted by Anders Mörtberg.

from itertools import count
import random

# We import the graphics.py library:
#
#   https://mcsp.wartburg.edu/zelle/python/graphics.py
#
# Note: this needs to be downloaded and saved in the same folder as
# this file for things to work!
#
from graphics import *


class Cell:
    """A class representing cells"""

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._friends = 0

    def coordinates(self):
        """Return the coordinates of the cell as a tuple"""
        return (self._x, self._y)

    def neighbors(self):
        """Returns the minesweeper neighbours of a cell, in a list.

        Returns:
            [list[Cell]]: a list of length 8, each element being a cell

        Example:
            Cell(2,3).neighbors() -> [C(1, 2), C(2, 2), C(3, 2)
                                      C(1, 3),          C(3, 3)
                                      C(1, 4), C(2, 4), C(3, 4)]
        """
        out = []
        for i in range(9):
            out.append((self._x - 1 + (i % 3), self._y - 1 + (i // 3)))
        out.remove((self._x, self._y))

        return [Cell(t[0], t[1]) for t in out]

    # Equality test for cells
    def __eq__(self, other):
        return self.coordinates() == other.coordinates()

    # Hash function for cells (necessary to use cells as keys in a dictionary)
    def __hash__(self):
        return self.coordinates().__hash__()

    def __str__(self) -> str:
        return "Cell(" + str(self._x) + ", " + str(self._y) + ")"

    def __repr__(self) -> str:
        return "C(" + str(self._x) + ", " + str(self._y) + ")"


def randomWorld(width, height, d=3):
    world = set()
    for x in range(width):
        for y in range(height):
            if random.randint(0, 10) < d:
                world.add(Cell(x, y))

    return world


print("randomworld", [c.coordinates() for c in randomWorld(10, 10)])

my_world = randomWorld(5, 5, 3)
print("hej", Cell(2, 3).neighbors())


def update(world):
    """Update the world by applying the rules of the game:

    1. Any live cell with two or three live neighbors survives.
    2. Any dead cell with three live neighbors becomes a live cell.
    3. All other live cells die in the next generation. Similarly,
       all other dead cells stay dead.
    """
    counter = dict()
    result = set()
    for c in world:
        for n in c.neighbors():
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

    for c in world:
        if c in counter and counter[c] in [2, 3]:
            result.add(c)

    for c in counter:
        if counter[c] == 3:
            result.add(c)

    return result

    # for c in world:


update(my_world)
## Extra functions for shifting and combining worlds


def shiftWorld(w, dx=0, dy=0):
    """Shift a world dx steps in x direction and dy steps in y direction"""
    out = set()

    for c in w:
        (x, y) = c.coordinates()
        out.add(Cell(x + dx, y + dy))

    return out


def unionWorlds(ws):
    """Compute the union of a list of worlds"""
    out = set()

    for w in ws:
        for c in w:
            out.add(c)

    return out


## Some fun starting worlds:

# One glider
# https://www.conwaylife.com/wiki/Glider
glider = {Cell(x, y) for (x, y) in [(2, 1), (3, 2), (1, 3), (2, 3), (3, 3)]}

print([x for x in update(glider)])
# Two gliders
# glider2 = unionWorlds([glider,shiftWorld(glider,10)])

# Many gliders and an obstacle
# manygliders = unionWorlds([ shiftWorld(glider,dx,dy)
#                             for dx in [0,10,20]
#                                 for dy in [0,10,20] ] +
#                           [ { Cell(x+32,30) for x in range(20) }])


## Code for displaying the world and running the animation


def display(width, height, world, win, rectangles):
    for x in range(width):
        for y in range(height):
            rectangles[y][x].setFill("black" if Cell(x, y) in world else "white")
    win.update()


## The main method
def main():
    # Number of iterations to run animation
    iterations = 1000

    # Size of squares
    k = 10

    # Width of window (will be multiplied by k)
    width = 60

    # Height of window (will be multiplied by k)
    height = 60

    # Create a window
    win = GraphWin("Game of Life", width * k, height * k, autoflush=False)

    # Create rectangles grid
    rectangles = [[Rectangle(Point(j * k, i * k), Point((j + 1) * k, (i + 1) * k)) for j in range(width)] for i in range(height)]

    # Draw rectangles in window
    for x in range(width):
        for y in range(height):
            rectangles[y][x].draw(win)

    # Initialize the world randomly
    world = randomWorld(width, height)

    # Uncomment to initialize with one glider
    # world = glider

    # Uncomment to initialize with two gliders
    # world = glider2

    # Uncomment to initialize with many gliders and an obstacle
    # world = manygliders

    # Run simulation "iterations" number of steps
    for i in range(iterations):
        # Draw the world
        display(width, height, world, win, rectangles)

        # Update the state of the world
        world = update(world)

    # Close the window and quit when we are done
    win.close()
    quit()


# Uncomment to run the animation
main()
