#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = (1,2,3)  # set is immutable
    y = [1,2,3]  # list is mutable
    s = 'string'

    y.append(5)
    y.insert(2,7)

    print(type(x),x)
    print(type(y),y)
    print(type(s),s[2:4])

    for i in x:
        print (i)

if __name__ == "__main__": main()
