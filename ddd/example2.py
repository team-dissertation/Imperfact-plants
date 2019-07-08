from ddd.painter2 import *

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


tree = Vine()
paint = Painter(tree)
paint.build_tree_set()
branches = paint.build_tree_set()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(0, 200)
plt.xlabel('x')
plt.ylabel('y')


for branch in branches:
    start = branch.start_point
    end = branch.end_point
    x = [start[0], end[0]]
    y = [start[1], end[1]]
    z = [start[2], end[2]]
    figure = ax.plot(x, y, z, c='r')

plt.show()


