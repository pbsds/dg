import dg; __builtins__.update(dg.BUILTINS)
print(1, (print(2) or 'A') in (print(3) or 'AA') in (print(4) or 'AA'))


def _2__lambda_():
    print(5, (print(6) or 7) < (print(8) or 9) < (print(10) or 11))
    return print(12, (print(13) or 14) >= (print(15) or 16) >= (print(17) or
        18), (print(13) or 14) >= (print(15) or 16) < (print(17) or 18))


_2__lambda_.__name__ = '<lambda>'
_2__lambda_.__qualname__ = '<lambda>'
_1 = foo = _2__lambda_


def _6__lambda_():
    import operator
    _4 = __builtins__['<'] = operator.lt
    import operator
    _5 = __builtins__['>'] = operator.gt
    print(19, __builtins__['<'](__builtins__['<'](print(20) or 21, print(22
        ) or 23), print(24) or 25))
    return print(26, __builtins__['>'](__builtins__['>'](print(27) or 28, 
        print(29) or 30), print(31) or 32), __builtins__['<'](
        __builtins__['>'](print(27) or 28, print(29) or 30), print(31) or 32))


_6__lambda_.__name__ = '<lambda>'
_6__lambda_.__qualname__ = '<lambda>'
_3 = bar = _6__lambda_
foo()
bar()
