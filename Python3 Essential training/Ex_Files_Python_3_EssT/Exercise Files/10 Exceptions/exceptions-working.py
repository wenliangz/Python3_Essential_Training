#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('xlines.txt') # if error raised here, the following line will not be excuted and directly to to except statement
    except IOError as e:
        print('could not open the file:',e)
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()
