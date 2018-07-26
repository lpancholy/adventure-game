import random
from point import Point

class Tree:
    def __init__(self, game_board):

        self.game_board = game_board

        unique_location = False

        while not unique_location: # generate random position & checks if there is another tree already constructed at that point
            self.location = Point(random.randint(0,8), random.randint(0,8))
            unique_location = True
            for tree in self.game_board.trees:
                if (tree.location == self.location):
                    unique_location = False
                    break

        self.game_board.trees.append(self)


    def speak(self):
        print("Hello peasant.")
