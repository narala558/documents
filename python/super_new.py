class Foo:
    def __init__(self):
        super().__init__()


class A:
    pass


class B(A):
    pass


class Bar(B):
    def __init__(self):
        super(A, self).__init__()