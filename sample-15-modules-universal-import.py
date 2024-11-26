# Modules are collections of functions. To use these functions, you need to import the module.
# There are 3 different ways to import:
# 1. Generic Import
# 2. Function Import
# 3. Universal Import
#
# This sample detail about Universal Import.
# In this example, every function is imported from the Random module.
# When calling the function(s), you don't need to specify the module name.


from random import *

print(randint(10,100))   # random integer being generated