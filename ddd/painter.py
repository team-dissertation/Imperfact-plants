import numpy
from ddd.model import *


class Painter(object):

    start_point = numpy.array([0, 0, 0])
    base_vector = numpy.array([0, 0, 10])
    tree_string = ''

    def __init__(self, tree):
        self.tree = tree

    def next_generation(self):
        if self.tree_string is None or self.tree_string is '':
            self.tree_string = self.tree.axiom
        rules = self.tree.rules
        variables = self.tree.variables
        temp_string = ''
        for item in self.tree_string:
            if item in variables:
                temp_string += rules[item]
            else:
                temp_string += item
        self.tree_string = temp_string
        print(self.tree_string)

    def build_tree_set(self):
        start_point = self.start_point
        vector = self.base_vector
        tree_string = self.tree_string
        angle = self.tree.angle
        save_point = []
        save_vector = []
        branch_list = []

        for item in tree_string:
            if item == 'F':
                end_point = start_point + vector
                branch = Branch(start_point, end_point)
                branch_list.append(branch)
                start_point = end_point
            elif item == 'f':
                start_point = start_point + vector
            elif item == 'A':
                pass
            elif item == 'S':
                pass
            elif item == 'L':
                pass
            elif item == '/':
                r_matrix = get_matrix('H', -angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '+':
                r_matrix = get_matrix('U', angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '-':
                r_matrix = get_matrix('U', -angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '&':
                r_matrix = get_matrix('L', angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '∧':
                r_matrix = get_matrix('L', -angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '|':
                r_matrix = get_matrix('U', math.pi)
                vector = numpy.dot(vector, r_matrix)
            elif item == '[':
                save_point.append(start_point)
                save_vector.append(vector)
            elif item == ']':
                start_point = save_point.pop()
                vector = save_vector.pop()
            else:
                pass
        return branch_list


def get_matrix(m_type, x):
    if m_type is 'U':
        RU = numpy.array(
            [
                [math.cos(x), math.sin(x), 0],
                [-math.sin(x), math.cos(x), 0],
                [0, 0, 1]
            ]
        )
        return RU
    elif m_type is 'L':
        RL = numpy.array(
            [
                [math.cos(x), 0, -math.sin(x)],
                [0, 1, 0],
                [math.sin(x), 0, math.cos(x)]
            ]
        )
        return RL
    elif m_type is 'H':
        RH = numpy.array(
            [
                [1, 0, 0],
                [0, math.cos(x), -math.sin(x)],
                [0, math.sin(x), math.cos(x)]
            ]
        )
        return RH
    else:
        raise RuntimeError('matrix type error')


tree = BushLike()
paint = Painter(tree)
paint.next_generation()
paint.next_generation()
branches = paint.build_tree_set()
