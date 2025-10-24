# Learn Interfaces by Building an Equation Solver by Mayra Silva
'''
I keep this files as I'm studying and taking notes throughout the code, feel free to see
how I decieded to solve some problems!
'''

from abc import ABC, abstractmethod


class Equation():
    def __init__(self):
        pass

    
    @abstractmethod
    def solve(self):
        pass
    @abstractmethod
    def analyze(self):
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