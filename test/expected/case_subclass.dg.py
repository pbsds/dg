import dg; __builtins__.update(dg.BUILTINS)
def _where_():
    _1 = a = 2
    print(_1)
    _2 = b = 3
    print(_2)
    return __builtins__['!subclass'](__builtins__['!locals'](), None,
        'None', 'None', '__name__', object)


print(1, _where_())


def _where_():
    _4 = a = 5
    print(_4)
    _5 = b = 6
    print(_5)

    def _7__lambda_(x):
        return str(7)
    _7__lambda_.__name__ = '<lambda>'
    _7__lambda_.__qualname__ = '<lambda>'
    _6 = __repr__ = _7__lambda_
    return __builtins__['!subclass'](__builtins__['!locals'](), None,
        'None', 'None', '__name__', object)


_3 = Foo = _where_()
print(4, _3)


def _where_():
    _9 = a = 9
    print(_9)
    _10 = b = 10
    print(_10)
    return __builtins__['!subclass'](__builtins__['!locals'](), None,
        'None', 'None', '__name__', Foo, int)


_8 = Bar = _where_()
print(8, _8)


def _where_():
    _12 = a = 12
    print(_12)
    _13 = b = 13
    print(_13)
    return __builtins__['!subclass'](__builtins__['!locals'](), None,
        'None', 'None', '__name__', Bar, metaclass=print)


_11 = Baz = _where_()
print(11, _11)
print(Foo())
print(Bar())
print(Baz == None)
