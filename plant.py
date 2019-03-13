import math


class Element(object):

    def next_generation(self, available):
        pass


class Branch(Element):
    x = 250
    y = 250

    def __init__(self, angle):
        self.length = 10
        self.angle = angle

    def make(self, father):
        if father:
            self.x = father.end_x
            self.y = father.end_y

        self.angle = self.angle % 360
        '''Keep for debug'''
        # if self.angle == 90:
        #     self.end_x = self.x
        #     self.end_y = self.y + self.length
        # elif self.angle == 180:
        #     self.end_x = self.x + self.length
        #     self.end_y = self.y
        # elif self.angle == 270:
        #     self.end_x = self.x
        #     self.end_y = self.y - self.length
        # else:
        #     self.end_x = self.x - self.length
        #     self.end_y = self.y
        self.end_x = self.x + self.length * math.cos(math.pi * (self.angle / 180))
        self.end_y = self.y + self.length * math.sin(math.pi * (self.angle / 180))


class KochCurve(object):
    # grammar F=F+F-F-F+F
    # axoim -F
    # angle 90

    grammar = 'F=F+F-F-F+F'
    axoim = '-F'
    angle = 90

    def __init__(self):
        self.treestr = self.axoim

    def next(self):
        self.treestr = self.treestr.replace('F', 'F+F-F-F+F')
        self.make()

    def make(self):
        temp = []
        for item in self.treestr:
            if item == '-':
                self.angle -= 90
            elif item == '+':
                self.angle += 90
            else:
                temp.append(Branch(self.angle))
        for index, item in enumerate(temp):
            if index == 0:
                item.make(father=None)
            else:
                item.make(father=temp[index - 1])
        self.trees = temp


if __name__ == '__main__':
    t = KochCurve()
    t.make()
    t.next()
    print(len(t.trees))
    t.next()
    print(len(t.trees))
