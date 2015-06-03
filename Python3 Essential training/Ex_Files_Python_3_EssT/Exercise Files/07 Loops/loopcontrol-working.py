#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c=='s': continue
        # if c=='s': break
        print(c, end='')
    else:
        print('else')

if __name__ == "__main__": main()


# else is also working for while

# def main():
#     s = 'this is a string'
#     i = 0
#   while(i < len(s))
#     for c in s:
#         if c=='s': continue
#         # if c=='s': break
#         print(c, end='')
#     else:
#         print('else')
#
# if __name__ == "__main__": main()