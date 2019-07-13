from ddd.painter2 import *
from ddd.bresenham3 import *

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

list=[]
count = 0
for branch in branches:
    start = branch.start_point
    end = branch.end_point
    x = [start[0], end[0]]
    y = [start[1], end[1]]
    z = [start[2], end[2]]
    #print(start[0],start[1],start[2])
    #print(end[0],end[1],end[2])
    point1=(int(start[0]),int(start[1]),int(start[2]))
    point2=(int(end[0]),int(end[1]),int(end[2]))
    cube_list=bresenham(point1, point2)
    #print(cube_list)

    for i in cube_list:
        if i in list:
            print("重合的方块是：")
            print(i)
            print("重合的坐标点是：")
            print(point1,point2)
        else:
            list.append(i)
            count+=1
    if count!=len(cube_list):
        print("该规则不合法")
    print(list)
    print(len(list))







    #figure = ax.plot(x, y, z, c='r')

#plt.show()



