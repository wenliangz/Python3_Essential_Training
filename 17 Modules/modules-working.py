#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

'''
read through python documentation
PyPi for tracking and install new packages
'''

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    # import os  # selectively import modules within function
    # print(os.name)
    # print(os.getenv('PATH'))
    # print(os.getcwd())
    # print(os.urandom(25))
    #
    # import urllib.request
    # page =urllib.request.urlopen('http://bw.org')
    # for line in page: print(str(line, encoding = 'utf_8'), end = '')

    # import random
    # print(random.randint(1,1000))
    # x = list(range(25))
    # print(x)
    # random.shuffle(x)
    # print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day,now.hour, now.minute, now.second, now.microsecond)


if __name__ == "__main__": main()
