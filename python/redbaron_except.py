import copy
import sys

from redbaron import RedBaron


in_file = out_file = sys.argv[1]

code = open(in_file).read()
red_baron = RedBaron(code)

try_nodes = red_baron.find_all('TryNode')


for node in try_nodes:
    if node.find('PassNode'):
        t_node = copy.copy(super_node)
        class_name = node.find_all('name')[1].name.dumps()

    while node.parent:
        node = node.parent
        if node.name == class_name:
            super_node.value[1] = '()'

with open(out_file, "w") as fh:
    fh.write(red_baron.dumps())
