Key Words
************
Variable
==========
A variable can be thought of as a labelled box. You store a value in the box
then you can refer to them later. When you assign a value to a variable you are changing
what is stored in it.

For example:
x = 5
x is the variable.

Assignment
==========
In coding, assignment is giving a value to a variable.

For example:
x = 5
5 is assigned to the variable x

Interpreter
==========
An interpreter takes a program written in a language that is human readable. This is because
in order for a computer to be able to execute your code it needs to be in a very different
format, google `machine code` if you're interested what it looks like. Machine code is known as
a low level language whereas Python is a high level language. This means that the interpreter
takes care of lots of things for you such as managing memory allocation.

For example Python and translates it into instructions that a computer can execute. An
interpreter does this line by line. This means if you have a 10 line program and a bug on
the 5th line the interpreter will execute lines 1 to 4 before an error is raised.

Namespace
==========
The namespace is a collection of all the available names that could be associated
with an object. You can think of a namespace as like a register. A register is a list of
all possible names a child in a class could have and each name is assigned to one
child only and uniquely identifies them.

Boolean
==========
A boolean is a type. It has only 2 possible values `true` or `false`.

Conditional Flow Control
==========
Flow control is the order in which the individual instructions that make up a
program are executed. Conditional flow control is when conditional execution
(if statements) is used to change the flow of the execution.

Syntax
==========
Syntax defines how to correctly structure your code. For example if you wrote

::

  >>> if 5 > 4
  ...     print "5 is more than 4"

You would get the following error:

::

  >>> if 5 > 4
  ...     print "5 is more than 4"
  File "<stdin>", line 1
    if 5 > 4
           ^
  SyntaxError: invalid syntax

This is because the code is incorrectly structured. All if statements must end with a colon.

Function
==========
A function is a block of instructions assigned to a name. For example:

::

  >>> def add_5_subtract_2(number):
  ...     return number + 5 - 2
  ...
  >>> add_5_subtract_2(7)
  10

Functions are useful as it means that you can reuse code. Every time you want to add
5 and subtract 2 from a number you can just call the function. This is particularly
useful if you are writing large complex functions as you don't have to type the code
out each time. Also it also makes it easier to find problems in your code.

Calling a Function
==========
Code inside a function does not run until the function is called. For example:

::

  >>> def say_hello(name):
  ...    return "Hello " + name
  ...
  >>> say_hello("Susie")
  Hello Susie

We have defined a function that gives instructions on how to say hello. However
we don't actually carry out the set of instructions until we call the function using:

::

>>> say_hello("Susie")

Parameters
==========
A parameter is additional information that is given to the function when it is called.
In this example the parameter is `number`
::
  >>> def add_5_subtract_2(number):
  ...     return number + 5 - 2

If a function has no parameters you will always get the same behaviour every time you
call it. A function is much more powerful if it has parameters. In the case of the
``add_5_subtract_2`` function you will get a different response depending on the
value of the parameter.

Bugs
==========
An error in code that causes the program to break or not behave as expected.

Debugging
==========
This is the process of finding errors in code and fixing them. Sometimes this is
easy sometimes it is very difficult and time consuming. Debugging your code with
someone else can often be very helpful.

Parentheses
==========
() These are parentheses. They are common syntax in many programming languages.
Parentheses can also be referred to brackets or braces.

Terminal
==========
There are two main ways to interact with a computer. The most common way is using a GUI.
A GUI is a Graphical User Interface and is focused around icons and mouse clicks.
The terminal is another way to interact with a computer. It is text based and
involves the user typing commands and the computer then displays a text response.
For example (for macs) open the terminal:

1. Press `Cmd(apple) + Spacebar` (the two keys together). A search box pops up.
2. Type `terminal` and press enter.
3. Type ``ls``

This will display a list of all the files and directories in your home directory.

Execute
==========
Execution is when a computer runs a series of code instructions.

Terminate
==========
A program has terminated when it has executed all instructions and stopped running.

Types
==========
Types are used to classify the data in a program. Some examples of types are `integer`
(whole numbers e.g. 5, 103), `boolean` (true or false), `string`(characters surrounded
by quotes e.g. "hello", "ID1453"). Types are useful as it allows us to understand
what we can do with data of this type for example it makes sense to divide one integer
by another but dividing one string by another doesn't make sense.

Types are also useful to understand how different bits of data within your program
can interact with each other. For example you can add two integers together and
get an answer however it is not possible to add a boolean to an integer as the two
types are not compatible.

Objects
==========
Objects in the real world have properties that describe them and actions they
can carry out. For example a dog is an object. A dog can be described in terms
of properties e.g. breed, colour, name etc. A dog also has actions that it can
carry out e.g. fetch, lie down, bark etc.

We also have objects in programming. These objects also have properties to describe
them and actions they can carry out. For example we may have an object that represents
a video. The video will have properties for example a title and how long it is. There will
also be actions on the video such as play and pause. In an object in programming
the properties are variables and the actions are functions.

An object can also be referred to as an `instance of a class`.

Class
==========
Classes and objects are very closely related. Classes are templates for creating objects.
It is likely that you will want multiple copies of the same type of object. For example
It is unlikely that you would only have one video you would want to have multiple video
objects all representing different videos. This is when you use a class. A class describes
what an object should look like. It determines what properties the object should have
and what actions it can carry out. This class is then used to create an object. The object
will have values for each of the properties. This is what make an object an `instance
of a class`, the class indicates what properties an object should have and each object
will have values for each one of these properties.

Operators
==========
An operator is a character or set of characters that represents an action. Some
examples of operators are ``+``, ``&&``, ``-``. Operators perform an action on operands.
For example in the case of the sum ``2 + 3``

``2`` and ``3`` are operands and ``+`` is the operator.
