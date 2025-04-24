#In this project, you will solve the mathematical puzzle 
# known as the Tower of Hanoi. 
# The puzzle consists of three rods and 
# a number of disks of different diameters.

NUMBER_OF_DISKS = 3
number_of_moves = (2 ** NUMBER_OF_DISKS) - 1

rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1),
    'B': [],
    'C': []
    }

# You can move only top-most disks
# You can move only one disk at a time
# You cannot place larger disks on top of smaller ones


def move(n, source, auxiliary, target):
    #display starting configuration
    print(rods)
    for move in range(number_of_moves):
        print(move)
    



#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')