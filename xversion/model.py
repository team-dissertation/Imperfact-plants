import math


class Branch(object):

    valid = True

    def __init__(self, start_point, end_point, symbol):
        self.start_point = start_point
        self.end_point = end_point
        self.symbol = symbol


class Vine(object):
    axiom = '--A'
    angle = 18 * math.pi / 180
    variables = ['A']
    rules = {
        '<A[++A]->A[--A]+<<A': 'A',
        '<A[+A]->A[-A]+<<A': 'A'
    }
