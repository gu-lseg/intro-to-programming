Names
*****

To work effectively with objects we need a way to refer to them.

Names are like the nouns we use in every day speach.

Names help: 

- make programming efficient. 
- capturing meaning. 


.. tip::

    If you find yourself needing to replace many similar values in order
    to update your code, using names is worth considering.

Assignment
==========

Naming integer objects::

    >>> x = 5
    >>> four = 4

Naming a string object::

    >>> first_name = "greg"

Unlike in maths, the equals symbol means assignment not equality.

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

What's in a name?
=================

A name doesn't exist in the environment. Its not an object. It is part of
the language (the code) that we use to refer to that world of objects. 

Just like the name 'greg' doesn't exist in the real world. It is a name that
refers to one or more objects of type persons.

In actuality a name is a symbol that is immediately replaced by the interpreter 
with an address in memory. A name points to an object's location in memory.

In a way it is synonmymous with the `id` of the object it refers to.

NameError
=========

If the interpreter gets a name that hasn't yet been defined it will complain
by throwing a `NameError`.

example::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined

Often typos lead to these types of errors.

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

Good naming
===========

The name `right_angle` was chosen to refer to an `int` of value 90. 

`thirty_degree_angle`, `angle`, or `dezwbpe` could be used and the code would work fine.

However:

* `thirty_degree_angle` is misleading
* `angle` is better, perhaps ok but vague
* `dezwbpe` is nonsense and conveys no meaning

By choosing appropriate names you make the code more readable.

Exercises
=========

Shapes
------

Refactor your code in `shapes.py` to use variables as much as possible.
