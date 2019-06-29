from ddd.model import *


class Painter(object):

    start_point = [10, 10, 10]
    base_vector = [0, 0, 10]
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

        a = 0
        for item in tree_string:

            if item == 'F' or item == 'A' or item == 'B' or item == 'C':
                end_point = [start_point[0] + vector[0], start_point[1] + vector[1], start_point[2] + vector[2]]
                branch = Branch(start_point, end_point)
                branch_list.append(branch)
                start_point = end_point
                a = a + 1
            elif item == 'f':
                start_point = start_point + vector
            elif item == 'S':
                pass
            elif item == 'L':
                pass
            elif item == '<': #rot x
                new_vector = [
                    vector[0],
                    vector[1] * math.cos(angle) - vector[2] * math.sin(angle),
                    vector[1] * math.sin(angle) + vector[2] * math.cos(angle)
                ]
                vector = new_vector
            elif item == '>': #rot -x
                new_vector = [
                    vector[0],
                    vector[1] * math.cos(-angle) - vector[2] * math.sin(-angle),
                    vector[1] * math.sin(-angle) + vector[2] * math.cos(-angle)
                ]
                vector = new_vector
            elif item == '+': #rot z
                new_vector = [
                    vector[0] * math.cos(angle) - vector[1] * math.sin(angle),
                    vector[0] * math.sin(angle) + vector[1] * math.cos(angle),
                    vector[2]
                ]
                vector = new_vector
            elif item == '-': #rot -z
                new_vector = [
                    vector[0] * math.cos(-angle) - vector[1] * math.sin(-angle),
                    vector[0] * math.sin(-angle) + vector[1] * math.cos(-angle),
                    vector[2]
                ]
                vector = new_vector
            elif item == '&': # rot y
                new_vector = [
                    vector[0] * math.cos(angle) + vector[2] * math.sin(angle),
                    vector[1],
                    vector[0] * math.sin(angle) + vector[2] * math.cos(angle)
                ]
                vector = new_vector
            elif item == '∧':
                new_vector = [
                    vector[0] * math.cos(-angle) + vector[2] * math.sin(-angle),
                    vector[1],
                    vector[0] * math.sin(-angle) + vector[2] * math.cos(-angle)
                ]
                vector = new_vector
            elif item == '|':
                new_vector = [
                    vector[0],
                    vector[1] * math.cos(math.pi) - vector[2] * math.sin(math.pi),
                    vector[1] * math.sin(math.pi) + vector[2] * math.cos(math.pi)
                ]
                vector = new_vector
            elif item == '[':
                save_point.append(start_point)
                save_vector.append(vector)
            elif item == ']':
                start_point = save_point.pop()
                vector = save_vector.pop()
            else:
                print('empty')
            print(vector)
        return branch_list


