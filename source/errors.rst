Errors
======

Errors and Exceptions are a constant feature of programming.

They always tell you what when wrong. They don't always tell you
why things went wrong though but in those cases they act as clues.

Learn to read errors first using intuition then by debugging and researchig. It
is a skill and it does get easier. Soon you will map errors to solutions very
quickly.

.. tip::

    You need to learn how to find information.
    Always read Errors and use your intuition, then Google.
    If that hsn't helped only then ask an expert. 

AttributeError
--------------

An `AttributeError` means the interpreter can't find the name you have asked
for on the object.

:: 

    >>> import turtle
    >>> turtle.shp('waef')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'shp'

Here the programmer has misspelt shape.

SyntaxError
-----------

Learning a language involves making many syntax (grammatical) errors.

A function defined badly::

    >>> def print_hi:
      File "<stdin>", line 1
        def print_hi 
                       ^
    SyntaxError: invalid syntax
    >>>

The programmer has forgotten that function definitions must have
parentheses `()` between the function name and the ending colon `:`.

::

    >>> def print_hi():
        print('hi')

No error this time. `print_hi` is properly defined.

