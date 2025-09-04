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
    

class R3Vector(R2Vector): #Child of R2Vector
    def __init__(self, x, y, z):
        super().__init__(x,y) # The super() function enables us to refer implicitly to the parent class, it is calling __ini__ from the parent class
        self.z = z


v1 = R2Vector(2,3)
print(v1.norm()) # to check if it is working
print(v1)

