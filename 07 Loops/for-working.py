#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

'''
for loop under the hood

First let’s look at the for loop under the hood.
When Python executes the for loop, it first invokes the __iter__() method of the container
to get the iterator of the container. It then repeatedly calls the next() method (__next__() method
in Python 3.x) of the iterator until the iterator raises a StopIteration exception.
Once the exception is raised, the for loop ends.

A couple of definitions

Iterable - A container is said to be iterable if it has the __iter__ method defined.
Iterator - An iterator is an object that supports the iterator protocol which basically means
that the following two methods need to be defined.
    It has an __iter__ method defined which returns itself.
    It has a next method defined (__next__ in Python 3.x) which returns the next value every time the next method is invoked on it.
For example consider a list. A list is iterable, but a list is not its own iterator.
'''

def main():
    '''/
    file object is an iterator, which is why it can only traverse the file once.
    You may reset the file cursor with .seek(0) as many have suggested.
    But you should, in most cases, only iterate a file once.
    '''
    fh = open('lines.txt')
    for line in fh: # for loop is to step through the iterator or container
    #for line in fh.readlines() # readlines() convert the iterator into a list variable(container)
        print(line, end = '')

if __name__ == "__main__": main()



# a = [1,2,3,4,5]
# it= iter(a)
# for i in a:
#     print (i)
#
#
# for i in it:
#     print (i)

# import os
# fh = open(os.path.join(os.getcwd(),'Ex_Files_Python_3_EssT\Exercise Files\\'+str('02') + ' Quick Start\lines.txt'))
# type(fh)




