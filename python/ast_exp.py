import ast


code = """
# this is a comment

def foo():
   print(
    "hello world"
)
"""

tree = ast.parse(code)
print(tree)


class GeneralVisitor(ast.NodeVisitor):

   def generic_visit(self, node):
     print(type(node).__name__, node)
     ast.NodeVisitor.generic_visit(self, node)

v = GeneralVisitor()
v.visit(tree)
