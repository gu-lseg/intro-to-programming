Interpreter & Debugging
***********************

Interpreter
===========

The interpreter parses the instructions in python code. It builds
representations or transforms the objects that are a direct cause 
of those instructions.

It translates the python code into another language called Bytecode. This
bytecode is interpreted on a virtual machine.

It isn't important to understand this in more detail at this stage.

So far we have seen that 2 types of objects that contain (or encapsulate) code:
`modules` and `functions`. There is a third type called a `class` more on that
later.

What is special about these 3 types of objects is that the interpreter
automatically creates a namespace for each of these.

https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

frames
======

A namespace is a mapping from names to objects.

The interpreter is responsible for maintaining the environment. This is
somewhat related to scope.

Programs execute over time. There is a definite time line during which
a program executes. Objects have a life cycle and a context.

To understand this you need to appreciate scope.

Name spaces

Visualising execution
=====================

It is very helpful to maintain a visualisation of what is happening.

Here are some tools to aid with developing that:

http://www.pythontutor.com/visualize.html#mode=edit
http://pyalgoviz.appspot.com/


Debugging
=========

A great way of interacting with a program and understanding what is going on.
Python includes `pdb` as standard.

To execute code with `pdb`::

    python3 -m pdb my.py

You can also pause the execution at any time by placing this line into your
code::

    import pdb; pdb.set_trace()

When you run your code normally (`python my.py`) the interpreter will break out
of the execution when it hits the line where you placed this.

This is very usefull to help you inspect what state the various objects of your
program are in at a given point in time.

Type `h` to get a list of all the commands. The important ones for now are:

These move line of execution:

* `l` print lines of code surrounding cursor
* `n` execute next line
* `s` step into a line. Typically used for entering functions.
* `c` continue till the end of the program (or next break point).

These are for examining the current location:

* `w` print frames on the stack at current position
* `u` go up a frame in stack
* `d` go down a frame in the stack

To exit:
* `q` exit the debugger. Will terminate program execution.


Exercise
========


pythontutor and pdb
-------------------

Whilst pythontutor is execellent as a pedagogical tool to demo small programs it isn't a proper
programmers tool. The programmer needs to visualise in her head.

We will use pythontutor.com and `pdb` together to exercise visualising program execution. 

Put this code into a file named `my.py`:: 
    
    x = 1
    y = 2
    success = 'increment function works'
    failure = 'increment function broken'

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

    python3 -m pdb my.py

You should see something like::

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

Copy the same code into www.pythontutor.com.

Step through each line of code keeping the visualiser tool and pdb in sync. Use
the visualiser as a map and find the various parts through pdb.

Ensure you explore the two frames when you enter the f functions' frame.

koans & pythontutor
-------------------

You can copy and paste any sample from the koans and use the pythontutor
visualiser to examine what is going on.

Choose one, preferrably that you found difficult to understand, and step
through it in the pythontutor visualiser.

koans & `pdb`
-------------

`pdb` is a great tool to understand code. Here we will apply it to our koans.

Drop `import pdb; pdb.set_trace()` at the beginning of a koan that caused you
difficulty. Step through the execution of the code. When you are done type `c`
to resume execution.


Optional: `inspect`
===================

There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the interpreter stack.

We are solely interested in examining the interpreter stack.

