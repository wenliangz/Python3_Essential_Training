#!/usr/bin/python3
# comments.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in primes(): # generate a list of prime numbers
        if n > 100: break
        print(n)

def isprime(n):
    if n == 1: #one is never prime by definition
        return False
    for x in range(2, n):
        if n % x == 0:
            return False # found a divisor, not prime
    else:
        return True

def primes(n = 1):
   while(True):
       if isprime(n): yield n # yield makes this a generator
       n += 1 

if __name__ == "__main__": main()
