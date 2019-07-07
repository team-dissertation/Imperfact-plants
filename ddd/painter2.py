import numpy
from ddd.model2 import *


class Painter(object):
    start_point = numpy.array([0, 0, 0])
    base_vector = numpy.array([0, 0, 10])
    tree_string = ''

    def __init__(self, tree):
        self.tree = tree

    def build_tree_set(self):

        last_string = self.tree_string
        if last_string is '':
            last_string = self.tree.axiom

        start_point = self.start_point
        vector = self.base_vector
        angle = self.tree.angle
        rules = self.tree.rules
        save_point = []
        save_vector = []
        branch_list = []
        new_string = ''

        for item in last_string:

            if item == 'F' or item == 'A' or item == 'B' or item == 'C':
                [rule_drawable, rule_start_point, rule_vector, rule_angle, rule_tree_string,
                 rule_branch_list] = self.check_rules(item, rules, start_point, vector)
                if rule_drawable:
                    start_point = rule_start_point
                    vector = rule_vector
                    angle = rule_angle
                    new_string = new_string + rule_tree_string
                    branch_list.extend(rule_branch_list)
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
        if item != 'F' and item != 'A' and item != 'B' and item != 'C':
            new_string = new_string + item
        self.tree_string = new_string
        return branch_list

    @staticmethod
    def check_rules(item, rules, start_point, vector, angle):
        save_point = []
        save_vector = []
        branch_list = []
        tree_string = ''
        rule_list = get_rule_list(rules, item)
        drawable = False
        if len(rule_list) == 0:
            rule_list = [item]
        for string in rule_list:
            for key in string:
                tree_string = tree_string + key
                if key == 'F' or key == 'A' or key == 'B' or key == 'C':
                    end_point = start_point + vector
                    branch = Branch(start_point, end_point, item)
                    # -------------------------------------------------------------
                    # here is the point that check whether the branch valid or not
                    # -------------------------------------------------------------
                    if not branch.valid:
                        tree_string == ''
                        break
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
            if tree_string != '':
                drawable = True
                break
        return [drawable, start_point, vector, angle, tree_string, branch_list]


# ulh
def get_matrix(m_type, x):
    t = ''
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
