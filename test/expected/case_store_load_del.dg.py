import dg; __builtins__.update(dg.BUILTINS)
_1 = ASD = 1


def _where_():

    def _where_():

        def _5__lambda_(self, key):
            print('get', key)
            return ASD
        _5__lambda_.__name__ = '<lambda>'
        _5__lambda_.__qualname__ = '<lambda>'
        _4 = __getattr__ = _5__lambda_

        def _7__lambda_(self, key, val):
            print('set', key, val)
            return ASD
        _7__lambda_.__name__ = '<lambda>'
        _7__lambda_.__qualname__ = '<lambda>'
        _6 = __setattr__ = _7__lambda_

        def _9__lambda_(self, key):
            print('del', key)
            return ASD
        _9__lambda_.__name__ = '<lambda>'
        _9__lambda_.__qualname__ = '<lambda>'
        _8 = __delattr__ = _9__lambda_
        _10 = __getitem__ = __getattr__
        _11 = __setitem__ = __setattr__
        _12 = __delitem__ = __delattr__
        return __builtins__['!subclass'](__builtins__['!locals'](), None,
            'None', 'None', '__name__', object)
    _3 = Obj = _where_()
    return Obj()


_2 = obj = _where_()
_13 = obj.foo = obj.bar
_14 = obj.foo, obj.bar = obj.bar, obj.foo
del obj.foo
_15 = obj[ASD] = ASD
del obj[ASD]
_16 = obj[ASD] = obj[ASD]
_17 = obj[ASD], obj[ASD] = obj[ASD], obj[ASD]
_18 = obj = obj[ASD]
print(ASD, _13, _14, None, _15, None, _16, _17, _18, obj, sep='\t')
_19 = self = 1
