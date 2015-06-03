#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(42,16)  # function argument must be initialized one way or the other.

def testfunc(number, another=43, onemore=75):
    #pass  # it is just place hold, not doing anything
    print('This is a test function',number,another,onemore)

if __name__ == "__main__": main()
