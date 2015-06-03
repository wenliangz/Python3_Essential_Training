#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a,b = 0,1
    a,b = b, a
    print(a,b)

if __name__ == "__main__": main()
