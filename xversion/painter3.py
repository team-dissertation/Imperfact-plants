from ddd.model import *
from math import sin, cos
from mathutils import Vector, Quaternion


class Turtle(object):
    axis_x = Vector([1, 0, 0])
    axis_y = Vector([0, 1, 0])
    axis_z = Vector([0, 0, 1])

    line = False

    def __init__(self, angle, other):
        if other is None:
            self.set_quaternions(angle)
            self.at = Vector([0, 0, 0])
            self.quaternion = Quaternion(self.at)
        else:
            self.at = other.at.copy()
            self.quaternion = other.quaternion.copy()

            self.yaw_add = other.yaw_add
            self.yaw_sub = other.yaw_sub
            self.roll_add = other.roll_add
            self.roll_sub = other.roll_sub
            self.pitch_add = other.pitch_add
            self.pitch_sub = other.pitch_sub

    def set_quaternions(self, angle):
        angle = angle * math.pi / 180

        v = Vector([0, 0, 0])
        self.yaw_add = Quaternion(v)
        self.yaw_add = self.set_angle(self.axis_z, angle, self.yaw_add)

        self.yaw_sub = Quaternion(v)
        self.yaw_sub = self.set_angle(self.axis_z, -angle, self.yaw_sub)

        self.roll_add = Quaternion(v)
        self.roll_add = self.set_angle(self.axis_y, angle, self.roll_add)

        self.roll_sub = Quaternion(v)
        self.roll_sub = self.set_angle(self.axis_y, -angle, self.roll_sub)

        self.pitch_add = Quaternion(v)
        self.pitch_add = self.set_angle(self.axis_x, angle, self.pitch_add)
        self.pitch_sub = Quaternion(v)
        self.pitch_sub = self.set_angle(self.axis_x, -angle, self.pitch_sub)

    @staticmethod
    def set_angle(axis, angle, quaternion):
        half_angle = angle / 2
        s = sin(half_angle)

        quaternion.x = axis.x * s
        quaternion.y = axis.y * s
        quaternion.z = axis.z * s
        quaternion.w = cos(half_angle)

        return quaternion

    def get_direct_vector(self):
        v = Vector([0, 1, 0])
        v = self.apply_quaternion(v, self.quaternion)
        return v

    @staticmethod
    def apply_quaternion(v, q):
        x = v.x
        y = v.y
        z = v.z
        qx = q.x
        qy = q.y
        qz = q.z
        qw = q.w

        ix = qw * x + qy * z - qz * y
        iy = qw * y + qz * x - qx * z
        iz = qw * z + qx * y - qy * x
        iw = - qx * x - qy * y - qz * z

        v.x = ix * qw + iw * - qx + iy * - qz - iz * - qy
        v.y = iy * qw + iw * - qy + iz * - qx - ix * - qz
        v.z = iz * qw + iw * - qz + ix * - qy - iy * - qx
        return v.copy()

    def extrude(self):
        self.at = self.at + self.get_direct_vector()
        return self.at.copy()

    def yaw_up(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.yaw_add)
        self.line = False

    def ywa_down(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.yaw_sub)
        self.line = False

    def roll_up(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.roll_add)

    def roll_down(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.roll_sub)

    def pitch_up(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.pitch_add)
        self.line = False

    def pitch_down(self):
        self.quaternion = self.mul_quaternions(self.quaternion, self.pitch_sub)
        self.line = False

    def get(self):
        return self.at.copy()

    @staticmethod
    def mul_quaternions(a, b):

        qax = a.x
        qay = a.y
        qaz = a.z
        qaw = a.w

        qbx = b.x
        qby = b.y
        qbz = b.z
        qbw = b.w
        a.x = qax * qbw + qaw * qbx + qay * qbz - qaz * qby
        a.y = qay * qbw + qaw * qby + qaz * qbx - qax * qbz
        a.z = qaz * qbw + qaw * qbz + qax * qby - qay * qbx
        a.w = qaw * qbw - qax * qbx - qay * qby - qaz * qbz
        return a


def get_branches(angle, tree_string):
    branch_list = []
    states = []
    working_branches = []
    state = Turtle(angle, None)

    working_branches.append([])
    working_branches[len(working_branches) - 1].append(state.get())

    for item in tree_string:
        if item == 'F' or item == 'A' or item == 'B' or item == 'C':
            pos = state.extrude()
            if state.line:
                working_branches[len(working_branches) - 1].pop()
            else:
                state.line = True
            working_branches[len(working_branches) - 1].append(pos.copy())
        elif item == '[':
            states.append(Turtle(angle, state))
            state.line = False
            working_branches.append([state.get()])
        elif item == ']':
            state = states.pop()
            bra = working_branches.pop()
            if len(bra) > 1:
                branch_list.append(bra)
        elif item == '+':
            state.yaw_up()
        elif item == '-':
            state.ywa_down()
        elif item == '>':
            state.roll_up()
        elif item == '<':
            state.roll_down()
        elif item == '&':
            state.pitch_up()
        elif item == '∧':
            state.pitch_down()
        else:
            pass

    branch_list.append(working_branches.pop())

    lists = []
    for item in branch_list:
        if len(item) <= 1:
            continue
        for i, d in enumerate(item):
            if i + 1 >= len(item):
                break
            if len(item) > 2:
                lists.append([d, item[i + 1], 'g'])
            else:
                lists.append([d, item[i + 1]])
    return lists


tree_string = '<<<<<<B<<<<<<B<<<<<<B<<<<<<B<<<<<<B[++<<<<B<<<<B[--][++][&&][^^][++<<B<<B[--][++][&&][^^][++BB[--C][++C][&&C][^^C]A]>>>>>+BBB[--C][++C][&&C][^^C]A]>>>>>+<<B<<B<<B[--][++][&&][^^][++BB[--C][++C][&&C][^^C]A]>>>>>+BBB[--C][++C][&&C][^^C]A]>>>>>+<<<<B<<<<B<<<<B[--][++][&&][^^][++<<B<<B[--][++][&&][^^][++BB[--C][++C][&&C][^^C]A]>>>>>+BBB[--C][++C][&&C][^^C]A]>>>>>+<<B<<B<<B[--][++][&&][^^][++BB[--C][++C][&&C][^^C]A]>>>>>+BBB[--C][++C][&&C][^^C]A'


angle = 18

branches = get_branches(angle, tree_string)

import matplotlib

matplotlib.use('tkagg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 15)

for index, branch in enumerate(branches):
    start = branch[0]
    end = branch[1]
    x = [start[0] + 10, end[0] + 10]
    z = [start[1], end[1]]
    y = [start[2] + 10, end[2] + 10]
    if len(branch) > 2:
        c = 'r'
    else:
        c = 'g'
    ax.plot(x, y, z, c=c)

plt.show()
