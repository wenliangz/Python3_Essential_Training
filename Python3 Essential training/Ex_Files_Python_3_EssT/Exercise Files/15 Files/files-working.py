#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    buffersize = 50000
    infile = open('bigfile.txt','r')
    outfile = open('new.txt','w')
    buffer = infile.read(buffersize)
    # open in buffer mode a bigger trunk in stead line by line.
    # Note that the read method on the file handle method is not iterable, so we can use for-loop here
    while len(buffer):
        outfile.write(buffer)
        print('.',end ='')
        buffer = infile.read(buffersize)
    print()
    print('Done.')

if __name__ == "__main__": main()
