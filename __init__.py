import os
import sys
import types

try:
    PY_TAG     = sys.implementation.cache_tag or 'unknown'
    PY_VERSION = sys.hexversion
    BUNDLE_DIR = os.path.join(__path__[0], 'bundle')
except AttributeError:
    raise ImportError('Python >= 3.4 required')

def load():
    from marshal import load

    try:
        with open(os.path.join(BUNDLE_DIR, PY_TAG + '.dgbundle'), 'rb') as fd:
            for code in load(fd):
                eval(code)
    except FileNotFoundError:
        def CodeTypeShim(*args):
            if hasattr(types.CodeType, 'co_posonlyargcount'):
                if len(args) == 15:  # posonlyargcount is missing (came from eariler version)
                    args = (args[0], 0, *args[1:])  # insert a posonlyargcount=0
            else:
                if len(args) == 15:  # posonlyargcount is present (came from later version)
                    args = (args[0], *args[2:])  # remove it
            return types.CodeType(*args)

        try:
            with open(os.path.join(BUNDLE_DIR, PY_TAG + '.dgbundle.py')) as fd:
                for code in eval(fd.read(), {'C': CodeTypeShim}):
                    eval(code)
        except FileNotFoundError:
            raise ImportError('python implementation {!r} not supported'.format(PY_TAG))

load()
