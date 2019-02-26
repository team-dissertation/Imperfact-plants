class Element(object):
    pass


class Branch(Element):

    def __init__(self):
        self.length = 1

    @staticmethod
    def next_generation():
        return [Branch(), Swerve(90), Branch(), Swerve(-90), Branch(), Swerve(-90),
                Branch(), Swerve(90), Branch()]


class Swerve(Element):

    def __init__(self, angle: int):
        self.angle = angle

    def next_generation(self):
        return [self]


class KochCurve(object):
    # grammar F=F+F-F-F+F
    # axoim -F
    # angle 90

    axoim = '-F'

    root = [Swerve(90), Branch()]
    trees = root

    def __init__(self, depth):
        self.branch = Branch
        self.depth = depth
        self.l_str = self.axoim

    def get_l_str(self):
        for i in range(1, self.depth):
            self.l_str = self.l_str.replace('F', 'F+F-F-F+F')
        return self.l_str

    def next(self):
        temp = []
        for i in self.trees:
            temp.extend(i.next_generation())
        self.trees = temp
        return self.trees


if __name__ == '__main__':
    t = KochCurve(2)
    t.next()
    print(len(t.trees))
    t.next()
    print(len(t.trees))
