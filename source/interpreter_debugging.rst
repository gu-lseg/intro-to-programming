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

frames
======

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


Exercise
========

Whilst pythontutor is execellent as a pedagogical tool to demo small programs it isn't a proper
programmers tool. The programmer needs to visualise in her head.

We will use pythontutor.com and `pdb` together to exercise visualising program execution. 

Put this code into a file named `my.py`:: 
    
    x = 1
    y = 2

    def inc(p):
        incremented = p + 1
        return incremented

    def print_result(result):

        success = 'increment function works'
        failure = 'increment function broken'

        if result:
            print(success)
        else:
            print(failure)


    inc_x = inc(x)
    result = inc_x == y
    print_result(result)



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


`inspect` (optional)
====================

Lets take a deeper look at what the interpreter does.
