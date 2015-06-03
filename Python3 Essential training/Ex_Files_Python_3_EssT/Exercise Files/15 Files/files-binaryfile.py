#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#Read and write binary file

def main():
    buffersize = 50000
    infile = open('olives.jpg','rb') #'rb' read in binary mode
    outfile =open('new.jpg','wb')
    buffer = infile.read(buffersize)

    while len(buffer):
        outfile.write(buffer)
        print ('.',end = '')
        buffer = infile.read(buffersize)


if __name__ == "__main__": main()
