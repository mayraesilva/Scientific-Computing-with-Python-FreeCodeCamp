#In this project, you will solve the mathematical puzzle 
# known as the Tower of Hanoi. 
# The puzzle consists of three rods and 
# a number of disks of different diameters.

NUMBER_OF_DISKS = 3
number_of_moves = (2 ** NUMBER_OF_DISKS) - 1

rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
    }

# You can move only top-most disks
# You can move only one disk at a time
# You cannot place larger disks on top of smaller ones

def make_allowed_move(rod1, rod2):
#rod1 = source and rod2 = target
    forward = False
    if len(rods[rod2]) == 0: #Here could also be if not rods[target]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
            
    if forward == True:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
            #after printing the move, we neet to remove from the source
            #and put it on the target
        rods[rod2].append(rods[rod1].pop())
            
    else: #when forward is false we have to move on the opposite direction
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    #display our progress
    print(rods, '\n')

def move(n, source, auxiliary, target):
    #display starting configuration
    print(rods, '\n')
    for move in range(number_of_moves):
        remainder = (move +1) % 3

        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {move + 1} allowed between {source} and {target}')
                make_allowed_move(source, target) 
            else:
                print(f'Move {move + 1} allowed between {source} and {auxiliary}')
                # make_allowed_move(source, auxiliary)                 

        elif remainder == 2:
            print(f'Move {move + 1} allowed between {source} and {auxiliary}')
            make_allowed_move(source, auxiliary)

        elif remainder == 0:
            print(f'Move {move + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)
    



#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')