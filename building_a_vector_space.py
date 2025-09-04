# Learn Special Methods by building a vector space by Mayra Silva


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        sum_squared_components = (self.x)**2 + (self.y)**2
        norm = (sum_squared_components)**(1/2)
        return norm
    


v1 = Vector(2,3)
print(v1.norm()) # to check if it is working
