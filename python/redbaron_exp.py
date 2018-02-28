import copy

from redbaron import RedBaron

red = RedBaron("some_value = 42")
red = RedBaron("x * True")

code = """
import time

time.sleep(10)

x = 1
y = x * 2
"""

code = """
def foo():
    return 1

foo()
"""

code = """# this is hello world
print('hello world')
"""

red = RedBaron(code)


code = open('super_old.py').read()

red_baron = RedBaron(code)

super_nodes = red_baron.find_all('AtomtrailersNode')


def refactor_super(node):
    while node.parent:
        pass


for super_node in super_nodes:
    node = copy.copy(super_node)
    class_name = node.find_all('name')[1].name.dumps()

    while node.parent:
        # print(node.name)
        node = node.parent
        if node.name == class_name:
            print(super_node.value[1])
            super_node.value[1] = '()'
            print(super_node)

with open("code.py", "w") as source_code:
    source_code.write(red_baron.dumps())
