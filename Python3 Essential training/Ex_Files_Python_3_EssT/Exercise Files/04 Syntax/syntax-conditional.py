#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#Condition excution:

# def main():
#     a, b = 1,1
#     if a<b:
#         print('a is less than b')
#     elif a > b:
#         print('a is greater than b')
#     else:
#         print('a is equal to b')
#
# if __name__ == "__main__": main()


# tThere is another form of conditional, which is condition expression or condition value

def main():
    a, b = 1, 1
    s = 'less than' if a < b else 'not less than'
    print(a, s, b)


if __name__ == "__main__": main()
