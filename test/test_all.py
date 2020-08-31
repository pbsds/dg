from dg import PY_TAG, PY_VERSION
import ast
import glob
import os.path as path
import pytest

CASE_DIR     = path.normpath(path.join(__file__, "..", "cases"))
EXPECTED_DIR = path.normpath(path.join(__file__, "..", "expected"))

CASES      = glob.glob(path.join(CASE_DIR, "case_*.dg"))
CASE_NAMES = list(map(path.basename, CASES))
EXPECTED   = [path.join(EXPECTED_DIR, i) for i in CASE_NAMES]
#EXPECTED   = [path.join(EXPECTED_DIR, "{}.{}.out".format(i, PY_TAG)) for i in CASES_NAMES]

@pytest.mark.parametrize("case,expected", zip(CASES, EXPECTED), ids=CASE_NAMES)
def test_run(case, expected, dg, code_runner, set_expected):
    expected += ".out"
    assert case != expected
    with open(case) as f:
        program = f.read()

    code = dg.compile(program, filename=case)
    out = code_runner(code)

    if not set_expected:
        with open(expected, "r") as f:
            assert out == f.read()
    else:
        with open(expected, "w") as f:
            f.write(out)

@pytest.mark.parametrize("case,expected", zip(CASES, EXPECTED), ids=CASE_NAMES)
def test_run_transpiler(case, expected, dg, code_runner):#, set_expected):
    expected += ".out"
    assert case != expected
    with open(case) as f:
        program = f.read()

    code = dg.transpile(program, filename=case, as_bytecode=True)
    out = code_runner(code)

    with open(expected) as f:
        assert out == f.read()
    # set_expected ignored here for now

@pytest.mark.parametrize("case,expected", zip(CASES, EXPECTED), ids=CASE_NAMES)
def test_python_output(case, expected, dg, set_expected):#, set_expected):
    expected += ".py"
    assert case != expected
    with open(case) as f:
        program = f.read()

    tree = dg.transpile(program, filename=case, as_bytecode=False)
    out = dg.asttree2python_source(tree)

    if not set_expected:
        with open(expected, "r") as f:
            assert out == f.read()
    else:
        with open(expected, "w") as f:
            f.write(out)
