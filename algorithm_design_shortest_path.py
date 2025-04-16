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
    'C': ['B', 'D'],
    'D': ['A', 'C']
}