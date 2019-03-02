import math


class Element(object):

    def next_generation(self, available):
        pass


class Branch(Element):

    def __init__(self, angle: int, father):
        self.length = 1
        if angle is None:
            raise Exception('angle can not be None')
        self.angle = angle
        if father is None:
            self.x = 0
            self.y = 0
        else:
            self.father = father
            self.x = father.end_x
            self.y = father.end_y
        self.end_x = self.x + self.length * math.cos(self.angle)
        self.end_y = self.y + self.length * math.sin(self.angle)

    def next_generation(self, available):
        if not available:
            return []
        b1 = Branch(father=self, angle=self.angle)
        b2 = Branch(father=b1, angle=b1.angle + 90)
        b3 = Branch(father=b2, angle=b2.angle - 90)
        b4 = Branch(father=b3, angle=b3.angle - 90)
        b5 = Branch(father=b4, angle=b4.angle + 90)

        return [b1, b2, b3, b4, b5]


class KochCurve(object):
    # grammar F=F+F-F-F+F
    # axoim -F
    # angle 90

    root = [Branch(angle=90, father=None)]
    trees = root

    def __init__(self):
        self.branch = Branch

    def next(self):
        temp = []
        for i in self.trees:
            temp.extend(i.next_generation(True))
        self.trees = temp
        return self.trees


if __name__ == '__main__':
    t = KochCurve()
    t.next()
    print(len(t.trees))
    t.next()
    print(len(t.trees))
