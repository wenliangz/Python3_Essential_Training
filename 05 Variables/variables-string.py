#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42
    s = r'This is a \n string!'  # r mean 'raw string', regular expression
    s = 'This is a {} string!'.format(n)  # new python 3 formatting string
    s = '''\
     this is a string
     line after line
     of text and more
     text''' # triple quote, this allows spand for multi-line, often used in a doc strings
    print(s)

if __name__ == "__main__": main()
