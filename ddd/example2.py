from ddd.painter2 import *


tree = Vine()
paint = Painter(tree)
branches = paint.build_tree_set()
print(paint.tree_string)
branches = paint.build_tree_set()
print(paint.tree_string)
print(branches)


