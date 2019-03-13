import math
from new.rules import *


class Point(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Color(object):
    r = 0
    g = 0
    b = 0


class Element(object):

    def next_generation(self, available):
        pass


class Branch(Element):

    color = Color()

    def __init__(self, angle, start_point, end_point):
        self.length = 10
        self.angle = angle
        self.start_point = start_point
        self.end_point = end_point


class Paint(object):

    tree_string = ''
    angle = 270
    branch = []
    save_point = []
    save_angle = []
    start_point = Point(350, 950)
    save = False
    length = 10

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
        self.start_point = Point(350, 950)
        self.angle = 270
        print(self.tree_string)
        self.make()

    def make(self):
        temp = []
        for item in self.tree_string:
            if item == '-':
                self.angle -= self.tree.angle
            if item == '+':
                self.angle += self.tree.angle

            if item == 'F' or item == 'A' or item == 'B' or item == 'G':
                self.angle = self.angle % 360
                start_point = self.start_point
                end_x = start_point.x + self.length * math.cos(math.pi * (self.angle / 180))
                end_y = start_point.y + self.length * math.sin(math.pi * (self.angle / 180))
                end_point = Point(end_x, end_y)
                temp.append(Branch(self.angle, start_point, end_point))
                self.start_point = end_point

            if item == '[':
                self.save_point.append(Point(self.start_point.x, self.start_point.y))
                self.save_angle.append(self.angle)
            if item == ']':
                p = self.save_point.pop()
                self.start_point = p
                angle = self.save_angle.pop()
                self.angle = angle

        self.branch = temp


if __name__ == '__main__':
    p = Paint(KochCurve())
    p.next_generation()
    p.next_generation()


