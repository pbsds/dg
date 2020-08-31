import dg; __builtins__.update(dg.BUILTINS)
import sys
import os
from os import path
import os
print(sys, os == os, __builtins__['!import'](__builtins__['!importname'](
    '/posixpath'), __builtins__['__package__'], False), path, os,
    __builtins__['!import'](__builtins__['!importname'](
    '/xml/etree/ElementTree'), __builtins__['__package__'], True), *sorted(
    locals().keys()), sep='\n')
