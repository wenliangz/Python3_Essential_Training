#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

## use one star argument, *arg, and two star variable(keyword argument) for passing arbitrary arguments to function

# *arg, pass as all remaining arguments as a tuple
# **kwarg, pass keyword arguments as a dic

def main():
    testfunc(1,2,3,4,5,6,7,one=1,two=2)

def testfunc(this, that, other, *args, **kwargs):
    print(this, that, other)
    print (args)
    print(kwargs)
    print(kwargs.get('one',default=None)) # use get method, returns default if key not in dict
    print(kwargs['two'])
    for n in args: print(n, end=' ')
    for n in kwargs: print(n, end=' ')

if __name__ == "__main__": main()


#
# def foo(*positional, **keywords):
#     print "Positional:", positional
#     print "Keywords:", keywords
# The *positional argument will store all of the positional arguments passed to foo(), with no limit to how many you can provide.
#
# >>> foo('one', 'two', 'three')
# Positional: ('one', 'two', 'three')
# Keywords: {}
# The **keywords argument will store any keyword arguments:
#
# >>> foo(a='one', b='two', c='three')
# Positional: ()
# Keywords: {'a': 'one', 'c': 'three', 'b': 'two'}
# And of course, you can use both at the same time:
#
# >>> foo('one','two',c='three',d='four')
# Positional: ('one', 'two')
# Keywords: {'c': 'three', 'd': 'four'}
# These features are rarely used, but occasionally they are very useful, and it's important to know which arguments are positional or keywords.