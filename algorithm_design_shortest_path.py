# #Exploring dictionaries

# copper = {'species' : 'guinea pig', 'age' : 2}

# copper['food'] = 'hay'
# copper['species'] = 'Cavia porcellus'

# print(copper)


# del copper['age']


# for i, j in copper.items():
#     print(i, j)

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node : 0 if node == start else float('inf') for node in graph}
    paths = {node : [] for node in graph}
    paths[start].append(start) #add the starting node to its own list

    while len(unvisited) != 0:
        current = min(unvisited) # to identify the closest, but it goes in alphabetic order

    
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')


#shortest_path(my_graph,'A')