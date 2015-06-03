#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


# a generator function is a function that return a iterator object! So this is how you create functionality
# that can be used in for ' for loop' or any other case that iterator is allowed

# def main():
#     print("This is the functions.py file.")
#     for i in inclusive_range(0,25,1):
#         print(i, end = ' ')
#
# def inclusive_range(start, stop, step):
#     i=start
#     while i <= stop:
#         yield i  # return i, but when next time the function is called, excution will continue right after the yield statement
#         i += step


# define a inclusive_range function that will work with only one argument
def main():
    print("This is the functions.py file.")
    for i in inclusive_range(25):
        print(i, end = ' ')

def inclusive_range(*args): #note non-default argument can not follow default argument, so we use *args to return tuple for parsing
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs ==1:
        stop = args[0]
        start = 0
        step =1
    elif numargs ==2:
        (start, stop) =args
        step =1
    elif numargs ==3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expect at most 3 arguments, got{}'.format(numargs))
    i= start
    while i <= stop:
        yield i  # return i, but when next time the function is called, excution will continue right after the yield statement,
        # while if it is return, excution will start the beginning of the function
        i += step

if __name__ == "__main__": main()
