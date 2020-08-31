import dg; __builtins__.update(dg.BUILTINS)
def _3__lambda_(pattern_0):
    _2 = a, b = pattern_0
    return a, head(str(b).split(' at 0x'))


_3__lambda_.__name__ = '<lambda>'
_3__lambda_.__qualname__ = '<lambda>'
_1 = x = _3__lambda_


def _6__lambda_(pattern_0):
    _5 = a, b = pattern_0
    return not str(a).startswith('_')


_6__lambda_.__name__ = '<lambda>'
_6__lambda_.__qualname__ = '<lambda>'
_4 = y = _6__lambda_
_7 = a = 1
print(_7)
_8 = b = 2
print(_8)


def _19__lambda_():
    _10 = a = 3
    print(_10)
    _11 = b = 4
    print(_11)
    _12 = c = 5
    print(_12)

    def _18__lambda_():
        _14 = a = 6
        print(_14)
        _15 = b = 7
        print(_15)
        _16 = c = 8
        print(_16)
        _17 = d = 9
        print(_17)
        return print(10, *sorted(map(x, filter(y, locals().items()))), sep='\n'
            )
    _18__lambda_.__name__ = '<lambda>'
    _18__lambda_.__qualname__ = '<lambda>'
    _13 = bar = _18__lambda_
    print(11, *sorted(map(x, filter(y, locals().items()))), sep='\n')
    bar()
    return print(12, *sorted(map(x, filter(y, locals().items()))), sep='\n')


_19__lambda_.__name__ = '<lambda>'
_19__lambda_.__qualname__ = '<lambda>'
_9 = foo = _19__lambda_
print(13, *sorted(map(x, filter(y, locals().items()))), sep='\n')
foo()
print(14, *sorted(map(x, filter(y, locals().items()))), sep='\n')
