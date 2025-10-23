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
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
        

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
        
        return NotImplemented
        
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        #My way of doing this comparison but could have replace all this by: return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        is_equal = []
        for i in vars(self):
            if getattr(self, i) == getattr(other, i):
                is_equal.append(True)
            else:
                is_equal.append(False)
        
        return all(is_equal)
    
    def __ne__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return not all(getattr(self, i) == getattr(other, i) for i in vars(self))
    
    def __lt__(self, other): #This method is called when we use < operador
        if type(self) != type(other):
            return NotImplemented
        
        return self.norm() < other.norm()
    
    def __gt__(self, other): #This method is called when we use > operador
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()
    
    def __le__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return not (self > other)
    
    def __ge__(self, other): #greater than/ equal
        return not self < other

class R3Vector(R2Vector): #Child of R2Vector
    def __init__(self,*, x, y, z):
        super().__init__(x=x,y=y) # The super() function enables us to refer implicitly to the parent class, it is calling __ini__ from the parent class
        self.z = z
    
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        
        kwargs = {
    'x': getattr(self, 'y') * getattr(other, 'z') - getattr(self, 'z') * getattr(other, 'y'),
    'y': getattr(self, 'z') * getattr(other, 'x') - getattr(self, 'x') * getattr(other, 'z'),
    'z': getattr(self, 'x') * getattr(other, 'y') - getattr(self, 'y') * getattr(other, 'x')
}
        return R3Vector(**kwargs)


v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * 3
print(f'v1 * 3 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

