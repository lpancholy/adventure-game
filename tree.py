import random
class Tree:
    def __init__(self, game_board):

        self.game_board = game_board

        unique_location = false
        while(!unique_location):
            # generate random position
            self.location = Point(random.randint(0,8), random.randint(0,8))
            for(tree in self.game_board.trees):
                if (tree.location == self.location):
                    

        # will need to put this in while statemenet somehow...




    def speak(self):
        # need to implement!
