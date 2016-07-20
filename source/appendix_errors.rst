Appendix B: Debugging
*********************

Exceptions occur when the interpreter can't carry out a given instruction. The
type of error (Exceptions are objects) communicates what is wrong.

We stress that most of programming is error driven. Don't think of errors negatively rather they are problem solving opportunities.

Debugging is working out what went wrong and fixing it.

Learn to be guided by Errors, and use debugging tools to master programming.

Here we explore some common errors and then we introduce `pdb` the python
debugger.

Errors
======

Errors always tell you what when wrong but not always why.

Read errors, first using intuition then by debugging and research. Google is
a very valuable resource when faced with an error, odds are you're not the first
person to come up against the problem.

.. tip::

    You need to learn how to find information.
    Always read Errors and use your intuition, then Google.
    If that hasn't helped only then ask an expert.

With time many errors map to solutions instantly.

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

Parentheses `()` are required after the name and the ending colon `:`.

::

    >>> def print_hi():
        print('hi')

No error, `print_hi` is properly defined.


pdb
===

pdb is the python debugger. You can freeze execution at a particular point in time, step through it, examining objects as you go.

To execute code with `pdb`::

    python -m pdb my.py

You can also pause the execution at any time by placing this line into your
code::

    import pdb; pdb.set_trace()

When you run your code normally (`python my.py`) the interpreter will break at
the that line of code.

Type `h` to get a list of all the commands. The important ones for now are:

Move along the execution timeline:

* `l` print lines of code surrounding cursor
* `n` execute next line
* `s` step into a line. Typically used for entering functions.
* `c` continue till the end of the program (or next break point).

Inspect the current location:

* `w` print frames on the stack at current position
* `u` go up a frame in stack
* `d` go down a frame in the stack

To exit:
* `q` exit the debugger. Will terminate program execution.


.. tip::

    On any error or exeception enter a `import pdb; pdb.set_trace()` on the line
    preceeding your program terminating. Run the program, then inspect what went wrong.

example
-------

We will use pythontutor hand in hand with pdb to exercise visualising program
execution.


Put this code into a file named `my.py`::

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



Execute with::

    python -m pdb my.py

`pdb` starts program and pauses at first line::

    > /Users/greg/my.py(1)<module>()
    -> x = 5
    (Pdb)

Executing `l` results in::

    (Pdb) l
      1  ->	x = 5
      2  	y = 6
      3
      4  	def f():
      5  	    z = 4
      6  	    total = sum(x, y, z)
      7  	    return total
      8
      9  	print('hi')
     10  	print(f())
    [EOF]

Step through each line of code keeping.

Ensure you explore the two frames when you enter the f functions' frame.

.. tip::
    We have used a python code visualiser in a similar way.
