#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

# Python programming language assumes any non-zero and non-null values as TRUE,
# and if it is either zero or null, then it is assumed as FALSE value.

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore',line)
        print (match)
        #print (re.sub('(Len|Neverm)ore', '###', line),end = '')
        if match:
            print(line.replace(match.group(),'###'), end='')

if __name__ == "__main__": main()
