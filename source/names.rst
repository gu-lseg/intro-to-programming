Names
*****

Names are like the nouns we use in every day speach.

::

    >>> tess = Turtle()


To work effectively with objects we need a way to refer to them. A person
object is always referred to by a name.

A name doesn't exist in the same way an object does. It is part of
the language (the code) that we use to refer to single objects in our
namespace (environment).

Likewise the name 'greg' doesn't exist in the world. It is a part of language that
refers to a single instance object of type Person.

Programmatically a name points to an object's location in memory. In a way it is 
synonmymous with the `id` of the object it refers to.

Similar to how we resolve 'greg' to the person in a room, when the interpreter
encouters a name it resolves that name by looking up the location in memory it
points to.

A name effectively tells the interpreter how to find the object you are referring to.

.. tip::

    Names and variables can be used interchangeably. We use 'name' because
    Python uses this terminology.

Assignment
==========

Unlike in maths, the equals symbol means assignment not equality.

Naming integer objects::

    >>> x = 5
    >>> four = 4

Naming a string object::

    >>> first_name = "greg"

The interpreter executes the code `x = 5` as:

* Create an object of type `int` of value 5
* Name that object `x`

From the point of definition onwards the programmer can now refer to that
object by using the name `x`.

Names can be reassigned to any type of object::

    >>> x = 5            # x refers to an `int` object
    >>> x = 'greg'       # x refers now to a `str` object 

A name is executed as an expression and it evaluates to its object::

    >>> x
    5

NameError
---------

If the interpreter gets a name that hasn't yet been defined it will complain
by throwing a `NameError`.

example::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined

These types of errors usually mean a typo.


User input
==========

To make programs interactive use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

When the interpreter meets `input` it:

1. prints the string message passed as an argument to `input`,
2. Buffers any characters typed
3. On the enter returns the characters as a new String.

Here the resultant string is assigned to the name `name`.

So if the user types in `Sophocles` then enter, a string obejct of value
'Sophocles' is assinged to name.


Reusability
===========

Names enhance a programmers' expressivity. They permit generalising code
thereby facilitating code reuse. Indeed they are often called variables.

Consider this code that draws a square with side length 50::

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

Now a decision is made that the sides be of length 100. 

You have to go back and replace 50 with 100 four times.

Using names you can do this::

    side = 50
    right_angle = 90

    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)

If you change your mind you need only update one value.

Note that our programatic definition mirrors the mathematical defintion in
that the lenguth of a square's side is irrelevant to its nature as a square.


.. tip::

    If you find yourself needing to replace many similar values in order
    to update your code, using names is worth considering.

Good Naming
-----------

The name `right_angle` was chosen to refer to an `int` of value 90. 

We could have used `thirty_degree_angle`, `angle`, or `awef` and the code would work fine. However:

* `thirty_degree_angle` is misleading its 90 not 30 degrees.
* `angle` is perhaps ok but a little vague
* `awef` is nonsense and conveys no meaning

By choosing appropriate names you make the code more readable and
intuitive.

Exercises
=========

names and values
----------------
::

    five = "five"

What does each set of characters on either side of the equal sign mean? 

Age in 2050
-----------

Write a program that asks the user for her age and prints how old she will be
in 2050.

Pay close attention to what the type of the objects you are dealing with are.

Shapes
------

Refactor your code in `shapes.py` to use variables as much as possible.
