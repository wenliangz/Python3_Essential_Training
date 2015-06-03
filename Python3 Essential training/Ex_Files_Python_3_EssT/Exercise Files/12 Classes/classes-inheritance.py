#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk(self): print ('I have something to say')
    def walk(self): print (' Hey! I'' walking here!')
    def clothes(self): print('I have nice closthes')

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()  # access the parent class
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
        print('I have brown and white fur')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()  # Override the one in parent class. Instead, if you want to incoperate, use super function

    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()


if __name__ == "__main__": main()
