# Learn Interfaces by Building an Equation Solver by Mayra Silva
'''
I keep this files as I'm studying and taking notes throughout the code, feel free to see
how I decieded to solve some problems!
'''

from abc import ABC, abstractmethod


class Equation():
    degree: int # you can annotate a variable to clarify that it will hold a specific data type
    def __init__(self):
        pass


    @abstractmethod
    def solve(self):
        pass


    @abstractmethod
    def analyze(self):
        pass


    def __init_subclass__(cls):
        pass

class LinearEquation(Equation):
    @abstractmethod
    def solve(self):
        pass
    @abstractmethod
    def analyze(self):
        pass


eq = Equation()
lin_eq = LinearEquation()