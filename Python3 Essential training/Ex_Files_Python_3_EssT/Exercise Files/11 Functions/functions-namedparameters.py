#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#function parameters
# 1.positional parameters that are mandatory
# 2.named, default value parameters that are optional.

def main():
    testfunc(5,6,7,8,9,10,one=1,two=2,four=42)

def testfunc(this, that, other, *args, **kwargs):
    # print('This is a test function',
    #       this, that, other, args,
    #       kwargs['one'],kwargs['two'],kwargs['four'])
    #for k in kwargs: print(k,kwargs[k])
    for n in args: print(n)

if __name__ == "__main__": main()
