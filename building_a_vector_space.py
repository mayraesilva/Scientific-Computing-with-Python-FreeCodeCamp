# Learn Special Methods by building a vector space by Mayra Silva


class R2Vector(): #Two dimensions vectors
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        sum_squared_components = (self.x)**2 + (self.y)**2
        norm = (sum_squared_components)**(1/2)
        return norm
    
    def __str__(self):
        vector = (self.x, self.y)
        return f'{vector}'
    


v1 = R2Vector(2,3)
print(v1.norm()) # to check if it is working
print(v1)

