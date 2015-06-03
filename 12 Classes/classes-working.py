#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

### classes are how you create your own objects
### A class is the blueprint for an object
### An object is an instance of a class, created from the blueprint of the class.
# Each objects encapsulate their own set of data and have their own data space


# methods is just the function under class. The first argument, self, is used to refer the object,but not the class
# in other words, when quack got called under donald object, the donald object get passed to the quack method
# Constructor is a special type of method: __init__. this get called every time you create a object based on the class
# Therefore, the most common purpose of constructor is to initialize some data.

# class Duck:
#     def __init__(self, value):
#         #print('constructor')
#         self._v = value
#
#     def quack(self):
#         print('Quaaack!',self._v)
#
#     def walk(self):
#         print('Walks like a duck.', self._v)
#
# def main():
#     donald = Duck(47) # create a donald object from class Duck
#     donald.quack() # '.' operator is used to reference to the quack attribute/method of the class Duck
#     donald.walk()
# if __name__ == "__main__": main()



# class Duck:
#     def __init__(self, color = 'white'):
#         self._color = color  # good idea use _color to indicate this will be used locally(methods within object) and not directly
#
#     def quack(self):
#         print('Quaaack!',self._v)
#
#     def walk(self):
#         print('Walks like a duck.', self._v)
#
#     def set_color(self,color):
#         self._color = color
#
#     def get_color(self):
#         return self._color
#
# def main():
#     donald = Duck()
#     print(donald.get_color())
#     donald.set_color('blue')
#     print(donald.get_color())
#
# if __name__ == "__main__": main()



# use keyword argument
class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs
        # used to store object data in dictionary variable attribute within its class, which allow a lot flexibility

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # def set_color(self,color):
    #     self.variables['color'] = color
    #
    # def get_color(self):
    #     return self.variables.get('color',None)
    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k,None)


def main():
    donald = Duck(feet=2)

    print(donald.variables)
    donald.set_variable('color', 'blue')
    print(donald.variables)
    print(donald.variables['color'])

    print(donald.get_variable('color'))
    print(donald.get_variable('feet'))

if __name__ == "__main__": main()
