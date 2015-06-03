#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Egg: #class is like a blue print, which defines how the object is created.
    def __init__(self, kind = 'fried'):  # this is a constructor
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()  #creat an object called 'fried', based on the class called "Egg".
    # The object encapsulate all the data and functions defined in the class.
    scrambled = Egg('scrambled')

    print(fried.whatKind())
    print(scrambled.whatKind())


if __name__ == "__main__": main()
