#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


#Polymorphic behaviour allows you to specify common methods in an "abstract" level,
# and implement them in particular instances.

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


def main():
    # create a list of objects
    animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]
    for animal in animals:
        print (animal.name + ': ' + animal.talk())


if __name__ == "__main__": main()
