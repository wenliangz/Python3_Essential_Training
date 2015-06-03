#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore',re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###',line), end='')

if __name__ == "__main__": main()
