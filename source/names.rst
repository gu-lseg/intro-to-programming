Names
*****

Here we look at:

* what assignment really means
* how to get input from a user
* how using names makes our code more useful.

.. tip::

    Names and variables can be used interchangeably. We use 'name' because
    Python uses this terminology.

Assignment
==========

Just like we need to name person objects to know how to differentiate between
them, `python3`, the interpreter, also needs to know what you are referring 
to when you give it instructions.

Assignment is one of the ways we associate names with objects.

.. tip::

    `=` the equals symbol means assignment and not equality (unlike in maths).

When the interpreter `python3` is launched it creates an empty namespace. A namespace is
where python stores names that refer to objects.

Assignment is how we tell the interpreter what names refer to.

::

    >>> x = 5

The interpreter executes the above code as:

1. Creates an `int` object with value 5.
2. Adds the name `x` to the current namespace.
3. Ensures the `x` name points to the created object.

From the point of assignment onwards the programmer can refer to that
object by using the name `x`.

A name is an expression and it evaluates to its object::

    >>> x
    5

Names can be reassigned to any type of object::

    >>> x = 5            # x refers to an `int` object
    >>> x = 'greg'       # x refers now to a `str` object 


The mysterious `from ... import ...` that we saw earlier is just about adding
names to the namespace so the interpreter knows what you are referring to::

    >>> from turtle import Turtle
    >>> tess = Turtle()


NameError
---------

If the interpreter gets a name that hasn't yet been defined through assignment 
it will complain by throwing a `NameError`.

example::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined

These types of errors often mean a typo.

Visualising Namespace
---------------------

Programmatically a name points to an object's location in memory. In a way it is 
synonmymous with the `id` of the object it refers to.

When the interpreter encouters a name it resolves that name by looking up the
location in memory it points to.

A name effectively tells the interpreter how to find the object you are referring to.

|py-tutor|

.. |py-tutor| raw:: html

    <iframe width="800" height="400" frameborder="0"
    src="http://pythontutor.com/iframe-embed.html#code=x+%3D+5%0Ax+%3D+'greg'%0Ax+%3D+5%0Aname+%3D+'greg'%0A%0Aresult+%3D+name+%3D%3D+'greg'%0A%0Aa_list+%3D+%5B'a',+'b',+'c'%5D&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400">
    </iframe>


As you can see for each assignment the namespace (frame) is updated:

* If the name already exists, 
* if its a new name, a new name is entered pointing to the object it is
  assigned to.

User input
==========

To make programs interactive use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

When the interpreter meets `input` it:

1. prints the string message passed as an argument to `input`,
2. Buffers (stores) any characters typed
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

Mathematics tells us a square's length can be of any size. Our
new programmatic definition mirrors that.

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
