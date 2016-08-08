Functions
*********

You can think of functions as actions, verbs, or commands
and you can think of parameters as adverbs, e.g. 'run, quickly'

Functions are special objects that contain code.

When you call them, using the special syntax `()`, you execute the
code they contain.

::

    >>> turtle.forward             # functions have names
    <function turtle.forward>
    >>> turtle.forward(10)         # actioned by use of '()'s


All turtle instructions are examples of calling functions attached
to the turtle object.

`print` is another function::

    >>> print('hello')

`print` simply prints its parameter to the console.

.. tip::

    Functions and methods are very similar.
    Methods exist on objects however functions stand alone.


Function objects
================

A function - like everything in Python - is an object. Function objects are different to
normal objects in that they contain blocks of code.

Functions help in letting programmers organise and reuse code. They help create useful abstractions.

Function objects - like normal variables - have names. The name is assigned at the same time you define a function.

defining
--------

Creating function objects requires special syntax::

    >>> def my_function():
    ...     print('hello')    # Note 4 space indentation
    ...
    >>> type(my_function)
    function

The ``def`` keyword is short for 'define' and is followed by the function object name, followed by () and then a colon.

example::

    def going_nowhere():
        turtle.forward(50)
        turlle.backward(50)

Note:

* The body of a function is the following block of code.
* A block is defined by a colon, and one or more indented lines.
* The indents are 4 spaces. The block ends on the first non indented line. (Take care to use spaces and not tabs for indenting)

Usage
-----

We 'call' functions by adding `()` at the end of their names.
This is syntax unique to functions. It means execute the function object's code block.


IndentationError
----------------

Indentation is the number of spaces from the left hand side. In python it defines blocks of code.

If you get this kind of error::

    >>> def awef():
    ... print('hi')
      File "<stdin>", line 2
        print('hi')
            ^
    IndentationError: expected an indented block

It simply means the indentation is wrong. Here the programmer has forgotten to
add 4 spaces before the line after the colon.


Arguments
=========

We saw that names can generalise code and ease code reuse. This is also true of functions that take arguments.

Compare this function without arguments::

    def draw_right_angle():
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)

to this one with arguments::

    def draw_right_angle(length):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)

The second function is more flexible. It can be used to move in a right-angle of any length,
whereas the first function function has the length of 10 'hardcoded' into the function.

An argument acts as a *variable* that is only defined inside the function's code block.

Functions can have many arguments::

    def move_diagonally(angle, length):
        turtle.left(angle)
        turtle.forward(length)


Function Scope
==============

We have seen two ways to add names to a namespace:

1. An assignment statement adds a name that references an object.
2. A function definition adds a name that references an object of type function.

Each function creates its own private namespace for the code it contains.

We will use pythontutor to exercise visualising program execution.

|py-function-ns|

.. |py-function-ns| raw:: html

    <iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=x+%3D+1%0Ay+%3D+2%0Asuccess+%3D+'works'%0Afailure+%3D+'broken'%0A%0Adef+inc(p)%3A%0A++++incremented+%3D+p+%2B+1%0A++++return+incremented%0A%0Adef+print_result(result)%3A%0A++++if+result%3A%0A++++++++print(success)%0A++++else%3A%0A++++++++print(failure)%0A%0Ainc_x+%3D+inc(x)%0Aprint_result(inc_x+%3D%3D+y)%0A&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400"> </iframe>

Step through each line of code in the browser.

Notice that when execution enters a function, a new 'frame' is created.

The interpreter creates a new namespace associated with this frame. It is
isolated from the 'parent' frame's namespace. This namespace is empty unless
arguments are passed.

.. tip::

    Technically, a namespace and a frame are different objects. For the purpose of this course
    however you can think of them as the same thing.


Exercises
=========


Shapes with Arguments
---------------------

Reopen ``shapes.py`` and define every shape as a function with sensible arguments.

Consider how this makes the code more modular, readable, reusable and general.

House
-----

Refactor (rewrite) your house code as a function that uses two other functions.


Conversion Programs
-------------------

This exercise assumes you have completed the `about_functions` koans.

For each conversion function you completed in the Koans, write a simple command
line program that prompts the user for input and returns the result.

For example with the function convert_to_miles, create a file named
`convert_miles_to_kilometers.py` and put your code in there.

Expect users to be able to run this kind of dialog::

    > python convert_miles_to_kilometers.py         # user runs program
    Please enter miles to convert: 34               # user enters 34
    34 miles corresponds to about 54.4 kilometers
    >

Do the same for celsius to farenheit.
