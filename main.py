from game_board import GameBoard
from tree import Tree
from character import Character
from direction import Direction

game_board = GameBoard()
for i in range(9):
    tree = Tree(game_board)

player = Character(game_board)

print(player.location)
user_dir = input("What direction would you like to move?").lower()
enum_dir = None
if ( user_dir == "north" ):
    enum_dir = Direction.NORTH
elif ( user_dir == "south" ):
    enum_dir = Direction.SOUTH
elif ( user_dir == "west" ):
    enum_dir = Direction.WEST
elif ( user_dir == "east" ):
    enum_dir = Direction.EAST

user_distance = int( input("How far would you like to move?") )
player.move(enum_dir, user_distance)
print(player.location)
