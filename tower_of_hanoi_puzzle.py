#In this project, you will solve the mathematical puzzle 
# known as the Tower of Hanoi. 
# The puzzle consists of three rods and 
# a number of disks of different diameters.

NUMBER_OF_DISKS = 3


rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
    }

# You can move only top-most disks
# You can move only one disk at a time
# You cannot place larger disks on top of smaller ones


def move(n, source, auxiliary, target):
    if n > 0:
        #  move n - 1 disks from source to auxiliary, so they are out of the way
        move(n-1, source, auxiliary, target)

        #as the rods change between source, target and auxiliary
        #we need to remove from one and put it on the other
        
        #move the nth disk from source to target
        rods[target].append(rods[source].pop())

        #display starting configuration
        print(rods, '\n')
    
    



#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')