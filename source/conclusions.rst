Conclusions 
***********

Abstractions
============

We have gone from step by step instructions to defining blocks of code in such
a way as to define higher level concepts.

Defining reusable components and the ability to repeat them is immensely powerful.

Think of everything you can make from Lego bricks. Minecraft is a world build
with cubes. In the real world think of all the components and repetition you
typically find in a skyscraper.

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.

Programming Constructs
======================

The constructs we have learnt (loops, conditions, data structures) mean that we
are far more expressive as programmers.

Combined with abstractions we can compose and recompose new programs.

Building on our previously defined concept of a house we now use repetition 
to define a row of houses.

:: 

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)

This is how complex and useful programs are built.

Object Oriented Programming
===========================

We have seen that Python offers a single compuational model. That of objects
using passing themselves to each others' methods.

There are other programming paradigms. Procedural, functional, and logic
programming exist. Object oriented is currently the most popular.

One aspect of object oriented programming we haven't explored is inheritance.

Polymorphism
============

Polymorphism means that different types respond to the same function.
Polymorphism is a fancy word that just means the same function is
defined on objects of different types. 

It makes programming more intuitive and therefore easier.

Python provides a set of special methods which are defined on many objects.
Some on all. 

These implement consistent behaviour for built in objects of different type.

Protocols enable:

* consistency - programmers can rely on intuition
* special syntax - interpreter translates nice syntax to functions on objects.


Exercises
=========

A Text editor
-------------

Think about the objects that you'd have to use to reprsent editing text.


Your Project
------------

Programmers model other domains. Think of an area where you are expert and
how you might code it.

What objects, functions and variables would need to be defined?
