#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


# A generator is  used in the context of iterable, ex. for loop
# we are going to create our own generator object for the use in the context of for-loop

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1:
            raise TypeError('requries at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('expected at most 3 arguments, got{}'.format(numargs))

    def __iter__(self):  # user __iter__ method in the class to make the object an iterable object
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
    # when iterable object used in a context of for-loop, the __iter__ method will get automatically called
    for i in inclusive_range(5, 25, 2): print(i, end=' ')


if __name__ == "__main__": main()
