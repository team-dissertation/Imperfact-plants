import numpy
from xversion.model import *

'''
每次都会给一整棵树，所以
'''


class Painter(object):
    start_point = numpy.array([0, 0, 0])
    base_vector = numpy.array([0, 0, 10])
    tree_string = ''
    n = 0

    def __init__(self, tree):
        self.tree = tree
        self.tree_string = tree.axiom

    # Every time this function called, the tree string will be renew
    def build_tree(self):
        rules = self.tree.rules
        variables = self.tree.variables
        tree_string = self.tree_string
        temp_string = ''
        if tree_string == '':
            raise RuntimeError('the tree string must not be none')
        for index, item in enumerate(tree_string):
            if item not in variables:
                temp_string = temp_string + item
                continue
            item_rules = get_rule_list(rules, item)
            rule = self.check_rules(item_rules, tree_string[index + 1:], temp_string, key=item)
            temp_string = temp_string + rule
        self.tree_string = temp_string
        branch_list = self.string_to_branch(temp_string)
        return branch_list

    def check_rules(self, item_rules, rest_string, front_string, key):

        rules = item_rules
        for rule in rules:
            string = front_string + rule + rest_string
            branch_list = self.string_to_branch(string)

            # This is the method to check the validation of rule
            valid = check_valid(branch_list)
            if valid:
                return rule

        return key

    def string_to_branch(self, tree_string):
        vector = self.base_vector
        start_point = self.start_point
        angle = self.tree.angle
        string = tree_string
        save_point = []
        save_vector = []
        branch_list = []

        for item in string:
            if item == 'F' or item == 'A' or item == 'B' or item == 'C':
                end_point = start_point + vector
                branch = Branch(start_point, end_point, item)
                branch_list.append(branch)
                start_point = end_point
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
            elif item == ']':
                start_point = save_point.pop()
                vector = save_vector.pop()
            else:
                pass
        return branch_list


def check_valid(branch_list):
    return True


def get_matrix(m_type, x):
    if m_type == 'H':
        t = numpy.array(
            [
                [math.cos(x), math.sin(x), 0],
                [-math.sin(x), math.cos(x), 0],
                [0, 0, 1]
            ]
        )
    elif m_type == 'L':
        t = numpy.array(
            [
                [math.cos(x), 0, -math.sin(x)],
                [0, 1, 0],
                [math.sin(x), 0, math.cos(x)]
            ]
        )
    elif m_type == 'U':
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


def get_rule_list(rules, key_word):
    rule_list = []
    for rule, key in rules.items():
        if key == key_word:
            rule_list.append(rule)
    return rule_list
