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

.. tip::

    Functions and methods are very similar. Methods exist on objects however functions stand alone.


Function objects
================

Just like everything else in Python a function is an object. Function objects are different in that they contain blocks of code.

Functions help in letting programmers organise and reuse code. They help create new abstractions.

Function objects have names. The name is assigned at the same time you define a function.

defining
--------

Creating function objects requires special syntax::

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

Indentation is the number of spaces from the left hand side. In python it defines blocks of code. 

If you get this kind of error::

    >>> def awef():
    ... print('hi')
      File "<stdin>", line 2
        print('hi')
            ^
    IndentationError: expected an indented block

It simply means the indentation wrong. Here the programmer has
forgotten to add 4 spaces on the new line after the colon.


Arguments
=========

We saw names generalise code and eases code reuse. This is also true of functions that take arguments.

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

The second function is more flexible. It can be used to move by any length.

The argument acts as a *variable* only defined inside the function's code block.

Functions can have many arguments:: 

    def move_diagonally(angle, length):
        turtle.left(angle)
        turtle.forward(length)

Scope & Namespaces
==================

We have seen two ways to add to a given namespace:

1. An assignment statement adds a name that references an object.
2. A function definition associates a name with an object of type function.

Functions however create a namespace that is relative only to its block of
code.

We will use pythontutor to exercise visualising program execution.

http://www.pythontutor.com/visualize.html#mode=edit

Copy this code into the browser editor::
    
    x = 1
    y = 2
    success = 'works'
    failure = 'broken'

    def inc(p):
        incremented = p + 1
        return incremented

    def print_result(result):
        if result:
            print(success)
        else:
            print(failure)

    inc_x = inc(x)
    print_result(inc_x == y)


Step through each line of code in the browser.

After stepping through a few times you will get something like this:

.. image:: /images/inc_visualisation.png


You will notice that when execution enters a function, a new 'frame' is
created. This frame is isolated from the previous frame.

In effect the interpreter creates a new namespace. This namespace is emtpy
unless parameters pass names and their values.

.. tip::

    A namespace and a frame are different objects. For the purpose of this course 
    however think of them as the same.

Programmatically a name points to an object's location in memory. In a way it is 
synonmymous with the `id` of the object it refers to.

When the interpreter encouters a name it resolves that name by looking up the
location in memory it points to.

A name effectively tells the interpreter how to find the object you are referring to.

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


Shapes with Arguments
---------------------

Reopen ``shapes.py`` and make new functions with sensible arguments.

Does this make the code more general and reusable?


House
-----

Refactor (rewrite) your house code as a function that uses two other functions.
