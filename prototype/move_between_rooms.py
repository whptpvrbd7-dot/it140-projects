"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Initially user will be placed in the main room or the Great Hall
starting_room = 'Great Hall'

# set current room to use in gameplay loop
currentRoom = starting_room

while True:
    # display current location
print('\nYou are currently in {}'.format(currentRoom))
# let thte user enter the command to move as 'go direction' or 'exit'


move = input("Enter your move: ").split()[-1].captialize()
print('--------------------------------)


#user to exit
      # if 'go direction' ==> 'direction'
      if move == Exit':
                # if exit ==> 'exit
print('Thank for playing the game. Hope you enjoyed it!")


# a valid move
if move in rooms [currentRoom]:
        currentRoom = rooms[currentRoom][move]


else:
    print('Invalid Move. You can't go that way!" .format(move))
