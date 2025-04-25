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
        remainder = (move +1) % 3

        if remainder == 1:
            print(f'Move {move + 1} allowed between {source} and {target}')

            forward = False
            if len(rods[target]) == 0: #Here could also be if not rods[target]:
                forward = True
            elif rods[source] and rods[source][-1] < rods[target][-1]:
                forward = True
            
            if forward == True:
                print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                #after printing the move, we neet to remove from the source
                #and put it on the target
                rods[target].append(rods[source].pop())
            
            else: #when forward is false we have to move on the opposite direction
                print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                rods[source].append(rods[target].pop())
            #display our progress
            #print(rods)

        elif remainder == 2:
            print(f'Move {move + 1} allowed between {source} and {auxiliary}')

         elif remainder == 0:
            print(f'Move {move + 1} allowed between {auxiliary} and {target}')
    



#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')