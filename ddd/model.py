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

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


class BushLike(object):
    axiom = 'A'
    angle = 22.5 * math.pi / 180
    variables = ['A', 'F', 'S', 'L']
    rules = {
        'A': '[&FL!A]/////%[&FL!A]///////%[&FL!A]',
        'F': 'S/////F',
        'S': 'FL',
        'L': '[%%%∧∧{-f+f+f-|-f+f+f}]'
    }
