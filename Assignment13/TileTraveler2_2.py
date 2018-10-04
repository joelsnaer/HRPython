# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def coinCheck(coins, col, row):
    userinput = ""
    if col == 1 and row == 2 or col == 2 and row == 2 or col == 2 and row == 3 or col == 3 and row == 2: # (1,2) (2,2) (2,3) (3,2)
        userinput = input("Pull a lever (y/n): ")
        if userinput.lower() == "y":
            coins += 1
            print("You received 1 coins, your total is now {}.".format(coins))
    return coins

def restart():
    while True:
        userinput = input("Play again (y/n): ")
        if userinput.lower() == "y":
            return True
        elif userinput.lower() == "n":
            return False
        else:
            print("Invalid input")

def play():
    victory = False
    row = 1
    col = 1
    coins = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        direction = input("Direction: ")
        direction = direction.lower()
        
        if not direction in valid_directions:
            print("Not a valid direction!")
        else:
            col, row = move(direction, col, row)
            victory = is_victory(col, row)
            if victory:
                print("Victory!")
                if restart():
                    return True
                else:
                    return False
            else:
                valid_directions = find_directions(col, row)
                coins = coinCheck(coins, col, row)
                print_directions(valid_directions)

def main():
    is_playing = True
    while is_playing:
        play()
        if play():
            is_playing = True
        else:
            is_playing = False
    

# The main program starts here
main()