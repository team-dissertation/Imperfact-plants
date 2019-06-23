from ddd.painter import *

tree = BushLike()
paint = Painter(tree)
paint.next_generation()
paint.next_generation()
branches = paint.build_tree_set()

'''
这里面是直线的列表，每条直线有三维空间下的起点和终点的坐标
'''
print(branches)
for branch in branches:
    print(branch.start_point)
    print(branch.end_point)
