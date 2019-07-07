import math

'''
F -- move forward at distance L(Step Length) and draw a line
f -- move forward at distance L(Step Length) without drawing a line
! -- multiply current thickness by dT(Thickness Scale)
A, B, C, D ... -- placeholders
L -- leaf
% -- increase color
+ -- RU(α)
- -- RU(-α)
& -- RL(α)
∧ -- RL(-α)
/ -- RH(α)
\ -- RH(-α)
| -- RU(180 degree)
'''


class Branch(object):

    valid = True

    def __init__(self, start_point, end_point, symbol):
        self.start_point = start_point
        self.end_point = end_point
        self.symbol = symbol


class BushLike(object):
    axiom = 'A'
    angle = 22.5 * math.pi / 180
    variables = ['A', 'F', 'S', 'L']
    rules = {
        'A': '[&FL!A]>>>>>%[&FL!A]>>>>>>>%[&FL!A]',
        'F': 'S>>>>>F',
        'S': 'FL',
        'L': '[<<<∧∧{-f+f+f-|-f+f+f}]'
    }


class BaTree(object):
    axiom = 'BBBBBA'
    angle = 18 * math.pi / 180
    variables = ['A', 'B', 'C']
    rules = {
        'A': '[++BB[--C][++C][&&C][^^C]A]>>>>>+BBB[--C][++C][&&C][^^C]A',
        'B': '$$B',
        'C': ''
    }


class Vine(object):
    axiom = '--A'
    angle = 18 * math.pi / 180
    variables = ['A']
    rules = {
        '<A[++A]->A[--A]+<<A': 'A',
        '<A[+A]->A[-A]+<<A': 'A'
    }
