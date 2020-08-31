import dg; __builtins__.update(dg.BUILTINS)
print(1, *sorted(globals().keys()), sep='\n2\t')
print(3, *sorted(locals().keys()), sep='\n3\t')
print(4, *sorted(__builtins__.keys()), sep='\n5\t')
print(6, *sorted(__builtins__['!import'](__builtins__['!importname'](
    '/builtins'), __builtins__['__package__'], False).__dict__.keys()), sep
    ='\n7\t')
