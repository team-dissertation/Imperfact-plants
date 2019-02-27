# "F" : Move forward a step of length d. A line segment between points (X,Y,Z) and (X',Y',Z') is drawn.
# "[" and "]": bracket - push and pop the current state , in this project it is used to generate the tree branchs.
# "+" : Turn left by angle Delta, Using rotation matrix R_U(Delta).
# "-" : Turn right by angle Delta, Using rotation matrix R_U(-Delta).
# "&" : Pitch down by angle Delta, Using rotation matrix R_L(Delta).
# "^" : Pitch up by angle Delta, Using rotation matrix R_L(-Delta).
# "<" : Roll left by angle Delta, Using rotation matrix R_H(Delta).
# ">" : Roll right by angle Delta, Using rotation matrix R_H(-Delta).
# " | " : Turn around, Using rotation matrix R_H(180).

# Start sting="F"
# Change string="F [- & < F][ < + + & F ] | | F [ - - & > F ] [+ & F ]"

# depth 3
# angle 22.5
from enum import Enum


class Element(object):

    def next_generation(self):
        pass


class Branch(Element):

    def __init__(self):
        self.length = 1

    def next_generation(self):
        # available = 2==2
        # if(available):
        #     pass
        return generate_list()


class Action(Enum):
    turn_left = 0
    turn_right = 1
    pitch_down = 2
    pitch_up = 3
    roll_left = 4
    roll_right = 5
    turn_around = 6


class Controller(Enum):
    start = 0
    end = 1


def generate_list():
    string = 'F[-&<F][<++&F]||F[--&>F][+&F]'
    lists = list(string)
    temp = []
    for i in lists:
        if i == 'F':
            temp.append(Branch())
        elif i == '[':
            temp.append(Controller.start)
        elif i == ']':
            temp.append(Controller.end)
        elif i == '-':
            temp.append(Action.turn_left)
        elif i == '+':
            temp.append(Action.turn_right)
        elif i == '<':
            temp.append(Action.pitch_down)
        elif i == '>':
            temp.append(Action.pitch_up)
        elif i == '&':
            temp.append(Action.roll_left)
        elif i == '^':
            temp.append(Action.turn_around)
        elif i == '|':
            temp.append(Action.turn_around)
    return temp


if __name__ == '__main__':
    generate_list()
