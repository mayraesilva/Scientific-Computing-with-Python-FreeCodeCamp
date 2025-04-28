#In this project, you will solve the mathematical puzzle 
# known as the Tower of Hanoi. 
# The puzzle consists of three rods and 
# a number of disks of different diameters.

NUMBER_OF_DISKS = 4


A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

# You can move only top-most disks
# You can move only one disk at a time
# You cannot place larger disks on top of smaller ones


def move(n, source, auxiliary, target):
    if n <= 0:
        return
        #  move n - 1 disks from source to auxiliary, so they are out of the way
    move(n-1, source, target, auxiliary)

    #as the rods change between source, target and auxiliary
    #we need to remove from one and put it on the other

    #move the nth disk from source to target
    target.append(source.pop())

    #display our progress
    print(A, B, C, '\n')

    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)

    



#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')