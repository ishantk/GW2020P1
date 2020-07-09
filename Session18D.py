# Importing a file from Package
# This will also execute __init__.py from the Package automatically

"""
import pack.One

pack.One.fun()
pack.One.show()
cRef = pack.One.CA()
"""

"""
import pack.One as o
o.fun()
o.show()
cRef = o.CA()
"""

"""
from pack.One import *
fun()
show()
cRef = CA()
"""

from pack.One import fun
from pack.One import CA

fun()
# show() # error
cRef = CA()
