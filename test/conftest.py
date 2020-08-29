# TODO: fix project structure, poetry also does not like it
import sys, os
sys.path.append( os.path.normpath(__file__ + "../../../..") )

from contextlib import redirect_stdout
from dg import PY_TAG, BUNDLE_DIR, PY_VERSION
import dg.core as core
import io
import pytest

def pytest_addoption(parser):
    parser.addoption("--set-expected", action="store_true",
        help="Write the current output from the tests in test/cases to test/expected")

def pytest_generate_tests(metafunc):
    if "set_expected" in metafunc.fixturenames:
        metafunc.parametrize("set_expected", [metafunc.config.option.set_expected])

class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

@pytest.fixture(scope="session")
def dg():
    # rebuild the dogelang core from source
    BUNDLE_TAG = 1337 # TODO: what is this
    old = core.load(PY_TAG, BUNDLE_DIR)
    this = list(core.build(old,  PY_TAG, PY_VERSION, BUNDLE_TAG))
    #this = list(core.build(this, PY_TAG, PY_VERSION, BUNDLE_TAG))
    #this = list(core.build(this, PY_TAG, PY_VERSION, BUNDLE_TAG))

    sandbox = {
        "PY_TAG"    : PY_TAG,
        "PY_VERSION": PY_VERSION,
    }
    for i in this:
        eval(i, sandbox)

    yield AttrDict(sandbox)


@pytest.fixture
def code_runner(dg):
    def callback(code):
        file = io.StringIO()
        with redirect_stdout(file):
            eval(code, {
                "__builtins__"    : dg.BUILTINS.copy(), # the dg module loader does this
                "__doc__"         : None,
                "__file__"        : "<string>",
                "__loader__"      : __loader__,
                "__name__"        : "__main__",
                "__package__"     : None,
                "__spec__"        : None,
            })
        return file.getvalue()
    yield callback
