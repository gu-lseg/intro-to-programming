Functions
*********

You can think of functions as actions, verbs, or commands and you can think of parameters as adverbs: 'run, quickly'

example::

    >>> turtle.forward             # functions have names
    <function turtle.forward>
    >>> turtle.forward(10)         # actioned by use of '()'s


All turtle instructions are examples of calling functions attached to the turtle object.

`print` is another function::
    
    >>> print('hello')

`print` simply prints its parameter to the console.


`function` type
===============

Function objects are special. They are objects that contain blocks of code.

Functions help in letting programmers organise and reuse code. They help create new abstractions.

Function objects have names. The name is assigned at the same time you define a function.

creating `function` types
-------------------------

::

    >>> def my_function():
    ...     print('hello')    # Note 4 space indentation
    ...
    >>> type(my_function)
    function

The ``def`` keyword is followed by the function object name, followed by () and then a colon. 

example::

    def going_nowhere():
        turtle.forward(50)
        turlle.backward(50)

Note:

* The body of a function is the following block of code.
* A block is defined by a colon, and one or more indented lines.
* The indents are 4 spaces. The block ends on the first non indented line. (Take care to use spaces and not tabs for indenting)

Functions defined on function objects::

    >>> dir(my_function)
    [ ... ]


We 'call' functions by adding `()` at the end of their names. This is syntax unique to functions. It means actioning the objects' code block.


IndentationError
----------------

Indentation is the number of spaces a piece of code is from the left hand side of
the page.

It is important in python. It defines blocks of code. A block of code is code
that goes together.

It is not unusual to get this kind of error::

    >>> def awef():
    ... print('hi')
      File "<stdin>", line 2
        print('hi')
            ^
    IndentationError: expected an indented block

It simply means we have gotten the indentation wrong. Here the programmer has
forgotten to add 4 spaces on the new line after the colon.



Parameters
==========

We saw that using names generalises code and facilitates code reuse. This is
also true of functions that use parameters.

Compare this function without parameters::

    def right_angle():
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)

to this one with parameters:: 

    def right_angle(length):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)

The second function is more flexible. It can be used to move by any length.

The parameter acts as a *variable* only defined inside the function's code block.

Functions can have many parameters::

    def move_diagonally(angle, length):
        turtle.left(angle)
        turtle.forward(length)

.. tip::

    parameters are also called arguments

Exercises
=========

documenting functions
---------------------

When you type::

    >>> help(turtle.forward)

What special method is being called on the method object forward?

Enter this into a file named `hello.py`::

    def hello():
        """ this function says hi """
        print('hi')

Now::

    >>> from hello import hello
    >>> help(hello)
    >>> hello.__doc__

Shapes
------

Reopen ``shapes.py`` and define every shape a function. Document your
functions.

Does this make the code more modular, readable, reusable?


Shapes with Paramaters
----------------------

Reopen ``shapes.py`` and make new functions with sensible parameters.

Does this make the code more general and reusable?


House
-----

Refactor (rewrite) your house code as a function that uses two other functions.
