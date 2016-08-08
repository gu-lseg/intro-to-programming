Functions
*********

A function is some code which has been given a name and which can be used
wherever you need it in your program. When we use a function we say we are
"calling" it.

Some examples of functions we've already used are ``print``, ``int`` and
``type``.

    >>> print("hello")
    hello
    >>> int("13")
    13
    >>> type(True)
    <type bool>

The ``print`` function simply prints out what is between the brackets. The
``int`` function turns something into an integer (in this example it's a
string "13"). The ``type`` function tells you the type of object something
is.

All of these functions only require one value, or "parameter", inside the
brackets. But some functions can be called with zero parameters, for example
the ``exit`` function:

    >>> exit()

Other functions require more than one parameter, for example the ``max``
function:

    >>> max(1, 2)
    2
    >>> max(-1000, 1000, 0)
    1000

.. tip::

   Like everything else in Python, functions are objects. Function objects
   contain code which you run using the brackets containing whatever parameters
   that function needs.


Defining and using functions
============================

Functions help you to organise your code better. You can split up complicated
tasks into several smaller, simpler ones. And they allow you to reuse code
without repeating it.

Definining functions
--------------------

Every function has to be "defined" before it can be used; functions have names
like variables. To define a function you use ``def``:

    >>> def say_hello(name):
    ...     print("hello " + name + "!")
    ...

The ``def`` keyword is followed by the function name, then the names of any
parameters the function requires inside brackets, and then a colon. On the
following lines you write the block of code for the function indented by four
spaces, like it's indented when you write an ``if`` or ``while`` block. We call
this a "definition".

Here's an example of a definition of a function called "going_nowhere" which
doesn't have any parameters:

    >>> def going_nowhere():
    ...     turtle.forward(50)
    ...     turtle.backward(50)
    ...

.. tip::

   It's important to indent the code in a function definition by four spaces. If
   you don't you'll see an error saying:

   ``IndentationError: expected an indented block``

Using functions
---------------

Once you've defined a function you can use, or "call", it as many times as you
need it by putting the function name followed by the brackets containing the
parameters the function requires.

    >>> say_hello("Barry")
    hello Barry!
    >>> say_hello("Paul")
    hello Paul!
    >>> going_nowhere()
    >>> exit()

Function parameters
===================

Function parameters make functions more flexible and useful. For example compare
this function for drawing a square without parameters::

    def draw_100_by_100_square():
        turtle.forward(100)
        turtle.left(90)
	turtle.forward(100)
        turtle.left(90)
	turtle.forward(100)
        turtle.left(90)
	turtle.forward(100)
        turtle.left(90)

to this one with an parameter called "size"::

    def draw_square(size):
        turtle.forward(size)
        turtle.left(90)
	turtle.forward(size)
        turtle.left(90)
	turtle.forward(size)
        turtle.left(90)
	turtle.forward(size)
        turtle.left(90)

The second function is more flexible; it can be used to draw a square of any
size. Here are some more examples of functions with parameters::
  
    def left_diagonal(angle, length):
        turtle.left(angle)
	turtle.forward(length)
        turtle.right(angle) # stay facing in the same direction

    def draw_polygon(side_length, sides):
        for _ in range(sides):
            turtle.forward(side_length)
	    turtle.left(360.0/sides)

.. tip::

   See what happens if you define a function with and parameter which has the
   same name as a variable in your program.

       >>> name = "Miss Moneypenny"
       >>> def witty_comeback(name):
       ...     print("Do you expect me to talk?")
       ...     print("No " + name + ", I expect you to die!")
       ...
       >>> witty_comeback("Mr Bond")
       Do you expect me to talk?
       No ??? I expect you to die!

Exercises
=========

Shapes
------

1. Open your "shapes.py" file and define every shape as a function with
   parameters.
2. Write a simple program which uses your new functions to check that they work.
3. Rewrite your program for drawing a house using your shape functions.


Conversions
-----------

4. Write a function called ``celsius_to_fahrenheit`` which has one parameter and
   converts a temperature in degrees celsius into the equivalent in degrees
   fahrenheit
   
   .. tip::

      Check Wikipedia to find out how to do this conversion --
      https://en.wikipedia.org/wiki/Fahrenheit#Definition_and_conversions

5. (Extension) Create a new program called "currency_converter.py" and copy the
   following code into it::

     import urllib2 import json

     def get_conversion_rate(base, to):
         response = urllib2.urlopen("http://api.fixer.io/latest?base=" + base + "&symbols=" + to)
	 data = json.loads(response.read())
	 return data["rates"][to]

   This defines a function called ``get_conversion_rates`` which fetches the
   current exchange rate between two currencies from the Internet. For example::

     >>> get_conversion_rate("USD", "GBP")
     0.751

   Your task is to make the currency_converter.py program work like this::

     $ python currency_converter.py
     What currency do you want to convert from? USD
     What currency do you want to convert to? GBP
     How much do you want to convert? 100
     100 USD = 75.1 GBP (exhange rate of 0.751)
