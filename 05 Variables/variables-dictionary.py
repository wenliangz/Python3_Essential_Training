#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Dictionary in python has the same idea as "associated array" or " Hash table" in other languages

def main():
    d = {'one':1,'two':2,'three':3,'four':4,'five':5}
    # another easy and better way to define dic, keyword augments to define dictionary object
    d = dict(
        one =1,two=2,three=3,four=4,five='five'
    )

    d['seven'] = 7
    for k in sorted(d.keys()):  # sort dict by key in alphabetic
        print(k,d[k])

if __name__ == "__main__": main()
