import random
class Character:
    def __init__(self, game_board):
        self.location = Point(random.randint(0,8), random.randint(0,8))
        self.lives = 3
        self.game_board = game_board
        self.sight_distance = 2

    def move(self, direction, distance):
        if(direction == Direction.NORTH):
            self.location.y += distance
        elif(direction == Direction.EAST):
            self.location.x += distance
        elif(direction == Direction.SOUTH):
            self.location.y -= distance
        elif(direction == Direction.WEST):
            self.location.x -= distance
        else:
            print("Pick north, south, east or west")

    def look(self):
        for(tree in self.game_board.trees):
            if tree.location.distance_to(self.location) <= self.sight_distance:
                print tree
