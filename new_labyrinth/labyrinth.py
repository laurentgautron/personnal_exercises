""" methods for labyrinth """
import random


class Labyrinth:

    def __init__(self):
        """ at first the labyrinth is full of '#' with list of tuples for coord and then i choice randomly a tuple in a
        side for exit(guardian) and make a path ( randomly) to the exit: replace '#' by ' ' """
        side = [(x, y) for x in range(1, 31) for y in range(1, 31) if (x in (1, 30)) or (y in (1, 30))]
        lab = {(x, y): "#" for x in range(1, 31) for y in range(1, 31)}
        guardian = random.choice(side)
        lab[guardian] = 'G'
        for x in range(1, 31):
            for y in range(1, 31):
                print(lab[(x, y)], end='')
            print()


labyrinth = Labyrinth()
