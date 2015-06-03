#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readfile('xlines.txt'): print(line.strip())
    except IOError as e:
        print('cannot read file:',e)
    except ValueError as e:
        print('bad filename', e)


def readfile(filename):
    if filename.endswith('txt'):
        fh=open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')

if __name__ == "__main__": main()
