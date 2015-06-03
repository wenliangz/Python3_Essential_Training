#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 0,1
    v = 'this is true' if a <b else 'this is not true'
    # if a < b:
    #     v = 'this is true'
    # else:
    #     v = 'this is not ture'
    print(v)

if __name__ == "__main__": main()
