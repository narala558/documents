def makebold(fn):
    def _bwrapper(*args, **kwargs):
        print('makebold called')
        return "<b>" + fn() + "</b>"
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return _bwrapper


def makeitalic(fn):
    def _iwrapper(x, y):
        print('iiiiiiiiiiiiiiiiiiiiii')
        return "<i>" + fn(x, y) + "</i>"
    return _iwrapper


@makebold
@makeitalic
def say(*args, **kwargs):
    print(args, kwargs)
    return "hello"


@makebold
def duh():
    print('duh')
    return 'duh'


duh()
duh('a')

# makebold( makeitalic(duh) ) ('a')
# makebold(duh)('a')


def tell(*args, **kwargs):
    print('ttttttttttttttttttttttttt')
    print(args, kwargs)
    print('ttttttttttttttttttttttttt')
    return "tell"


# print(say('a', 'b'))

print( makebold(tell)('a', x='x') )


# def say():
#     return "hello"



# print(say())
