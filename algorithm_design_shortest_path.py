#Exploring dictionaries

copper = {'species' : 'guinea pig', 'age' : 2}

copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

print(copper)

for item in copper.items():
    print(item)