# Alternative for from package_a.module1 import Module1
# Below import works as the actual imports are done in __init__.py
from package_a import Module1
from package_a import Module2

print(Module1())
print(Module2())
