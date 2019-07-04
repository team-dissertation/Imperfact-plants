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
        current_father = ''
        save_upper_nodes = []

        for item in tree_string:

            if item == 'F' or item == 'A' or item == 'B' or item == 'C':
                end_point = start_point + vector
                branch = Branch(start_point, end_point)

                if current_father is not '':
                    branch.father = current_father
                current_father = branch

                branch_list.append(branch)
                start_point = end_point
            elif item == 'f':
                start_point = start_point + vector
            elif item == 'S':
                pass
            elif item == 'L':
                pass
            elif item == '>':
                r_matrix = get_matrix('H', -angle)
                vector = numpy.dot(vector, r_matrix)
            elif item == '<':
                r_matrix = get_matrix('H', angle)
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
                if current_father is not '':
                    save_upper_nodes.append(current_father)
            elif item == ']':
                start_point = save_point.pop()
                vector = save_vector.pop()
                current_father = save_upper_nodes.pop()
            else:
                pass
        return branch_list


#ulh
def get_matrix(m_type, x):
    t = ''
    if m_type is 'H':
        t = numpy.array(
            [
                [math.cos(x), math.sin(x), 0],
                [-math.sin(x), math.cos(x), 0],
                [0, 0, 1]
            ]
        )
    elif m_type is 'L':
        t = numpy.array(
            [
                [math.cos(x), 0, -math.sin(x)],
                [0, 1, 0],
                [math.sin(x), 0, math.cos(x)]
            ]
        )
    elif m_type is 'U':
        t = numpy.array(
            [
                [1, 0, 0],
                [0, math.cos(x), -math.sin(x)],
                [0, math.sin(x), math.cos(x)]
            ]
        )
    else:
        raise RuntimeError('matrix type error')
    return t

