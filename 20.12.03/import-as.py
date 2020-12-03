#import python_package.utils
#from python_package.utils import say_twice

#from python_package.talk import human
#from python_package.talk import animal
#from python_package.talk import *

#print(animal.sing())
#print(animal.cry())

#r = u.say_twice('hello')
#print(r)

#print(human.sing())
#print(human.cry())

try:
    from python_package import utils
except ImportError:
    from python_package.tools import utils

utils.say_twice('word')