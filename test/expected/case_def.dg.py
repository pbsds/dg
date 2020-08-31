import dg; __builtins__.update(dg.BUILTINS)
from inspect import signature
_1 = arun = __builtins__['!import'](__builtins__['!importname']('/asyncio/'
    ), __builtins__['__package__'], False).get_event_loop().run_until_complete


def _2__lambda_(a, b, c):
    return print(1)


_2__lambda_.__name__ = '<lambda>'
_2__lambda_.__qualname__ = '<lambda>'


def _3__lambda_(a, b, c):
    print(2)
    print(3)
    print(4)
    return print(5)


_3__lambda_.__name__ = '<lambda>'
_3__lambda_.__qualname__ = '<lambda>'


def _4__lambda_(*foo, bar, baz=2):
    return print(6)


_4__lambda_.__name__ = '<lambda>'
_4__lambda_.__qualname__ = '<lambda>'


def _5__lambda_(foo, bar=1, baz=2):
    return print(7)


_5__lambda_.__name__ = '<lambda>'
_5__lambda_.__qualname__ = '<lambda>'


def _6__lambda_(foo, *bar, **baz):
    return print(8)


_6__lambda_.__name__ = '<lambda>'
_6__lambda_.__qualname__ = '<lambda>'


def _7__lambda_():
    return print(9)


_7__lambda_.__name__ = '<lambda>'
_7__lambda_.__qualname__ = '<lambda>'


async def _8__lambda_():
    return print(10)


_8__lambda_.__name__ = '<lambda>'
_8__lambda_.__qualname__ = '<lambda>'


async def _9__lambda_():
    return print(11)


_9__lambda_.__name__ = '<lambda>'
_9__lambda_.__qualname__ = '<lambda>'


def _10__lambda_(a):
    return print(12)


_10__lambda_.__name__ = '<lambda>'
_10__lambda_.__qualname__ = '<lambda>'


async def _11__lambda_(a):
    return print(13)


_11__lambda_.__name__ = '<lambda>'
_11__lambda_.__qualname__ = '<lambda>'


async def _12__lambda_(a):
    return print(14)


_12__lambda_.__name__ = '<lambda>'
_12__lambda_.__qualname__ = '<lambda>'


def _13__lambda_(self, a):
    return print(15)


_13__lambda_.__name__ = '<lambda>'
_13__lambda_.__qualname__ = '<lambda>'


async def _14__lambda_(self, a):
    return print(16)


_14__lambda_.__name__ = '<lambda>'
_14__lambda_.__qualname__ = '<lambda>'


async def _15__lambda_(self, a):
    return print(17)


_15__lambda_.__name__ = '<lambda>'
_15__lambda_.__qualname__ = '<lambda>'
print(*map(signature, [_2__lambda_, _3__lambda_, _4__lambda_, _5__lambda_,
    _6__lambda_, _7__lambda_, _8__lambda_, _9__lambda_, _10__lambda_,
    _11__lambda_, _12__lambda_, _13__lambda_, _14__lambda_, _15__lambda_]),
    sep='\n')


def _16__lambda_():
    return print(18)


_16__lambda_.__name__ = '<lambda>'
_16__lambda_.__qualname__ = '<lambda>'
_16__lambda_()


def _17__lambda_(self):
    return print(19)


_17__lambda_.__name__ = '<lambda>'
_17__lambda_.__qualname__ = '<lambda>'
print(type(property(_17__lambda_)))


def _18__lambda_(self):
    return print(20)


_18__lambda_.__name__ = '<lambda>'
_18__lambda_.__qualname__ = '<lambda>'
print(type(property(_18__lambda_)))


async def _19__lambda_(self):
    return print(21)


_19__lambda_.__name__ = '<lambda>'
_19__lambda_.__qualname__ = '<lambda>'
print(type(property(_19__lambda_)))


def _20__lambda_(a):
    return None


_20__lambda_.__name__ = '<lambda>'
_20__lambda_.__qualname__ = '<lambda>'
print(_20__lambda_('hello'))


def _21__lambda_(a):
    return 23


_21__lambda_.__name__ = '<lambda>'
_21__lambda_.__qualname__ = '<lambda>'
print(_21__lambda_('hello'))


def _22__lambda_(self, a):
    return None


_22__lambda_.__name__ = '<lambda>'
_22__lambda_.__qualname__ = '<lambda>'
print(_22__lambda_('hello', 'world'))


def _23__lambda_(self, a):
    return 24


_23__lambda_.__name__ = '<lambda>'
_23__lambda_.__qualname__ = '<lambda>'
print(_23__lambda_('hello', 'world'))


async def _24__lambda_(a):
    return None


_24__lambda_.__name__ = '<lambda>'
_24__lambda_.__qualname__ = '<lambda>'
print(arun(_24__lambda_('hello')))


async def _25__lambda_(a):
    return 25


_25__lambda_.__name__ = '<lambda>'
_25__lambda_.__qualname__ = '<lambda>'
print(arun(_25__lambda_('hello')))


async def _26__lambda_(self, a):
    return None


_26__lambda_.__name__ = '<lambda>'
_26__lambda_.__qualname__ = '<lambda>'
print(arun(_26__lambda_('hello', 'world')))


async def _27__lambda_(self, a):
    return 26


_27__lambda_.__name__ = '<lambda>'
_27__lambda_.__qualname__ = '<lambda>'
print(arun(_27__lambda_('hello', 'world')))


async def _28__lambda_(a):
    return None


_28__lambda_.__name__ = '<lambda>'
_28__lambda_.__qualname__ = '<lambda>'
print(arun(_28__lambda_('hello')))


async def _29__lambda_(a):
    return 27


_29__lambda_.__name__ = '<lambda>'
_29__lambda_.__qualname__ = '<lambda>'
print(arun(_29__lambda_('hello')))


async def _30__lambda_(self, a):
    return None


_30__lambda_.__name__ = '<lambda>'
_30__lambda_.__qualname__ = '<lambda>'
print(arun(_30__lambda_('hello', 'world')))


async def _31__lambda_(self, a):
    return 28


_31__lambda_.__name__ = '<lambda>'
_31__lambda_.__qualname__ = '<lambda>'
print(arun(_31__lambda_('hello', 'world')))
