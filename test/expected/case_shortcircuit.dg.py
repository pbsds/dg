import dg; __builtins__.update(dg.BUILTINS)
print(1, (print(2) or print(3)) or print(4))
print(5, print(6) and (print(7) and print(8)))
print(9, (print(10) and print(11)) and print(12))
print()
print(13, ((print(14) or 15) or (print(16) or 17)) or (print(18) or 19))
print(20, (print(21) or 22) and ((print(23) or 24) and (print(25) or 26)))
print(27, ((print(28) or 29) and (print(30) or 31)) and (print(32) or 33))