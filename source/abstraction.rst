Conclusions 
***********

Abstractions
============

Defining reusable components and the ability to repeat them is imensely powerful.

Think of everything you can make from Lego bricks. Minecraft is a world build
with cubes. In the real world think of all the components and repetition you
typically find in a skyscraper.

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.

Building on layers of details you can construct palaces.

These are phsical and familiar to us. Just think of what you can do with basic building blocks.

Programmers model many other domains. Think of an area where you are expert and
how you might code it.

What objects, functions and variables would need to be defined?

Building on our previously defined concept of a house we now use repetition 
to define a row of houses.

:: 

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)


Polymorphism
============

Polymorphism means that different types respond to the same function.

Polymorphism is very useful as it makes programming more intuitive and
therefore easier.

Polymorphism is a fancy word that just means the same function is
defined on objects of different types. 

Python provides protocols which is polymorphism under the hood. These implement consistent behaviour 
for built in objects of different type.

Protocols
---------

When we introspect an object we have a lot of attributes that take this format:
`__names__`. This section will make many of those clear.

Everything is an object and all actions ultimately mean calling functions defined on objects.

Protocols are polymorphic functions that are embbedded into python. Most
importantly the interpreter is aware of them.

Protocols enable:

* consistency - programmers can rely on intuition
* special syntax - interpreter translates nice syntax to functions on objects.


Exercises
=========

Any Shape
---------

Write code that draws this:

.. image:: /images/turtle-all-shapes.png

.. tip::

    The sum of the external angles of any shape is always 360 degrees.
