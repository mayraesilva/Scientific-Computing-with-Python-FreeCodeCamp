# Learn Interfaces by Building an Equation Solver by Mayra Silva
'''
I keep this files as I'm studying and taking notes throughout the code, feel free to see
how I decieded to solve some problems!
'''

from abc import ABC, abstractmethod


class Equation(ABC):
    degree: int # you can annotate a variable to clarify that it will hold a specific data type
    
    
    def __init__(self, *args): #depending on the equation, we may need to pass a variable number of args
        if (self.degree + 1) != len(args):
            raise TypeError(f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments but {len(args)} were given")
        
        # for arg in args:
        #     if not isinstance(arg, (int,float)):
        #         raise TypeError("Coefficients must be of type 'int' or 'float'")

        #Another way to say the same is:
        if any( not isinstance(arg,(int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        
        if args[0] == 0: #Remember that the highest degree coefficient should be passed as the first argument when instantiating the object.
            raise ValueError('Highest degree coefficient must be different from zero')
        
        self.coefficients = {self.degree - index : coefficient for index, coefficient in enumerate(args)}
        # above there is a dict comprehension to get the coefficients and its degrees associated


    def __init_subclass__(cls):
        if not hasattr(cls, 'degree'):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")
    
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if coefficient == 0:
                continue
            if n == 0: # If n == 0, the term is made by the coefficient itself.
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x')

        equation_string = ' '.join(terms).strip('+') + ' = 0'
        return equation_string


    @abstractmethod
    def solve(self):
        pass


    @abstractmethod
    def analyze(self):
        pass

class LinearEquation(Equation):
    degree = 1 #This attribute represents the degree of the equation
    
    def solve(self):
        a,b = self.coefficients.values()
        x = - b / a
        return x
    
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept' : intercept}

#eq = Equation()
lin_eq = LinearEquation(2, 3)
print(lin_eq.solve())