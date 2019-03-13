'''
F -- move forward
G -- move forward
A -- move forward
B -- move forward

X -- means nothing
Y -- means nothing

C -- means need to change color
0 -- color r: 140 g: 80  b: 60
1 -- color r: 24  g: 180 b: 24
2 -- color r: 48  g: 220 b: 48
3 -- color r: 64  g: 255 b: 64
'''


class Color(object):

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Tree(object):

    variables = []
    rules = {}
    axiom = ''
    color = [Color(0, 0, 0)]
    angle = 90


class KochCurve(Tree):

    def __init__(self):
        self.axiom = '-F'
        self.rules = {'F': 'F+F-F-F+F'}
        self.variables = ['F']
        self.angle = 90


class KevTrees(Tree):

    def __init__(self):
        self.axiom = 'F'
        self.rules = {'F': 'C0FF-[C1-F+F+F]+[C2+F-F-F]'}
        self.variables = ['F']
        self.angle = 22


class KevsWispyTree(Tree):

    def __init__(self):
        self.axiom = 'FX'
        self.rules = {'F': 'C0FF-[C1-F+F]+[C2+F-F]', 'X': 'C0FF+[C1+F]+[C3-F]'}
        self.variables = ['F', 'X']
        self.angle = 25
        self.color = [Color(140, 80, 60), Color(24, 180, 24), Color(48, 220, 48), Color(64, 255, 64)]


class FractalPlant(Tree):

    def __init__(self):
        self.axiom = 'X'
        self.rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
        self.variables = ['F', 'X']
        self.angle = 22.5
        self.color = [Color(140, 80, 60), Color(24, 180, 24), Color(48, 220, 48), Color(64, 255, 64)]
