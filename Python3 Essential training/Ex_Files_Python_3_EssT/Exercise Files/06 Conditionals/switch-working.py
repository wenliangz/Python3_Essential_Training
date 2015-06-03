#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict(
        one='first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )

    v ='three'
    w ='six'
    print(choices[v])
    print(choices.get(w,'other'))  # use get method to avoid non-existing value in dict


if __name__ == "__main__": main()
