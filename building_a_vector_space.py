# Learn Special Methods by building a vector space by Mayra Silva


class R2Vector(): #Two dimensions vectors
    def __init__(self,*, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (sum(val**2 for val in vars(self).values()))**0.5 # we changed from __dict__ to improve readability
    
    def __str__(self):
        vector = (self.x, self.y)
        return f'{vector}'
    

class R3Vector(R2Vector): #Child of R2Vector
    def __init__(self,*, x, y, z):
        super().__init__(x=x,y=y) # The super() function enables us to refer implicitly to the parent class, it is calling __ini__ from the parent class
        self.z = z


v1 = R2Vector(x=2,y=3)
print(v1.norm()) # to check if it is working
print(v1)

v2 = R3Vector(x=2,y=2,z=3)
print(v2) #for us to see how it is affected when we get different dimensions
print(v2.norm())

print(v1.__dict__)
print(v2.__dict__)  # the __dict__ atribute is a dictionary that sotres the objects attibutes

print(v1.norm())
print(v2.norm())

