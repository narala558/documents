import ast

import astor


code = """
# this is a comment

def foo():

   print(
    "hello world"
)
"""

tree = ast.parse(code)

ast = astor.to_source(tree)

print(ast)
