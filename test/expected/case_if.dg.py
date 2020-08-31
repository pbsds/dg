import dg; __builtins__.update(dg.BUILTINS)
print(1, print(3) or 4 if print(2) else 9 if print(5) else None)
print(10, print(12) or 13 if 11 else 18 if print(14) else None)
print(19, print(21) or 22 if print(20) else print(24) or 25 if print(23) else
    30 if 26 else None)
print(31, print(33) or 34 if print(32) else print(36) or 37 if 35 else None)
print(38, print(40) or 41 if 39 else print(43) or 44 if print(42) else None)
