# Learn Special Methods by building a vector space by Mayra Silva


class R2Vector(): #Two dimensions vectors
    def __init__(self,*, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (sum(val**2 for val in vars(self).values()))**0.5 # we changed from __dict__ to improve readability
    
    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self))) # getattr is a bult-in function
    
    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'
    
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        
        kwargs = {i : getattr(self,i) + getattr(other, i) for i in vars(self) }
        return self.__class__(**kwargs)
    
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        

    def __mul__(self, other):
        if type(other) == int or type(other) == float: #when a vector is multiplied by a number
            kwargs = {}
            for key, val in vars(self).items():
                kwargs[key] = other * val
            return self.__class__(**kwargs)
        
        elif type(self) == type(other): # dot product
            coordinates = [getattr(self,i) * getattr(other,i) for i in vars(self)]           
            result = sum(coordinates)
            return result
        
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)


class R3Vector(R2Vector): #Child of R2Vector
    def __init__(self,*, x, y, z):
        super().__init__(x=x,y=y) # The super() function enables us to refer implicitly to the parent class, it is calling __ini__ from the parent class
        self.z = z


v1 = R2Vector(x=2, y=3)
v2 = R2Vector(x=0.5, y=1.25)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')