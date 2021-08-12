# With these imports in __init__ , Module1, Module2 class can be imported
# directly from package_a, without mentioning the module file name
# This helps in hiding the long import statements.
from package_a.module1 import Module1
from package_a.module2 import Module2
