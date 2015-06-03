#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


#Python programming language assumes any non-zero and non-null values as TRUE,
# and if it is either zero or null, then it is assumed as FALSE value.


def main():
    a, b = 0,1
    if a > b:
        print('this is true')
    elif a:
        print('a is zero or null')
    elif b:
        print('b is not zero or null')
    elif a == b:
        print ('a equals b')
    else:
        print ('it is not true')

if __name__ == "__main__": main()
