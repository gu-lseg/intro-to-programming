Names
*****

In this section we will examine names and assignment more closely.

.. tip::

    Names and variables in this context are synonyms. We use 'name' because
    Python uses this terminology.

Assignment
==========

Assignment is one of the ways we associate names with objects. Names are how 
the interpreter knows to locate what programmers are referring to.

Just like we need to name person objects to know how to differentiate between
them, `python3`, the interpreter, also needs to know what you are referring 
to when you give it instructions.

.. tip::

    `=` the equals symbol means assignment and not equality (unlike in maths).

::

    >>> x = 5

The interpreter executes the above code as:

1. Create an `int` object of value 5.
2. Does `x` exist in the namespace?

    True  - update the name `x` to point to the new `int` object.

    False - create a new name `x` in the namespace and make it point to the new object.


From the point of assignment onwards code can refer to that
object by using the name `x`. The interpreter will know how to find it by
looking up the value in the namespace.

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


Visualising
-----------

|py-tutor|

.. |py-tutor| raw:: html

    <iframe width="800" height="400" frameborder="0"
    src="http://pythontutor.com/iframe-embed.html#code=x+%3D+5%0Ax+%3D+'greg'%0Ax+%3D+5%0Aname+%3D+'greg'%0A%0Aresult+%3D+name+%3D%3D+'greg'%0A%0Aa_list+%3D+%5B'a',+'b',+'c'%5D&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400">
    </iframe>


For each assignment:

* If the name already exists, the namespace (frame) is updated.
* If the name doesn't exist, a new name is created pointing and it references 
  the newly created object.


NameError
---------

If the interpreter gets a name that hasn't yet been defined through assignment 
it will complain by throwing a `NameError`.

example::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined


Questions
---------
::

    five = "five"

What does each set of characters on either side of the equal sign mean? 


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

Age in 2050
-----------

Write a program that asks the user for her age and prints how old she will be
in 2020.

Shapes
------

Refactor your code in `shapes.py` to use variables as much as possible.


Objects & Types Q&A
===================

If you understand the answers to these you understand everything about objects and types!!

.. tip::
    Use the interpreter to help you find answers


Describe in detail what the interpreter does when you type the following and
enter:: 

    >>> '5'

    >>> 5

What is the result this line of code?::

    3 < '5'


Instances of both `str` and `int` objects recognise the `+` symbol. What output would you expect of the following lines of code?

::

    '1' + '2'

    1 + 2


Try the same above but this time using `*` instead of `+`. What can you
conclude of the meaning of `*`?
