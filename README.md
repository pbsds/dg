# woof

dg to CPython byte-compiler.

## Fatal Flaws

1. `try/except/else/finally`, `with`, `for/else`, `break`, `continue`, and the `else` clause of `while` are missing.
2. Methods lack `__class__` cell; `super` needs both arguments to work correctly.
3. Syntax can be awful sometimes.

## Documentation

Oh, and there's no documentation since the syntax is not very stable yet.

