Interpreter & Debugging
***********************

The interpreter does a lot of work in the background that we don't see. Some of
it we don't need to know about. But other parts is essential to programming.

Programs execute over time. There is an execution timeline during which objects and names have a life cycle and a context.

Debugging exposes the work that the interpreter does that is relevant to the
programmer. It enables interacting with the timeline of execution and the execution environment.

Note a lot of this is out of the scope of this course and we will cut corners. The aim is to get an intuition for what is going on and not to be exact. 

Runtime
=======

The runtime can be seen as a timeline of execution from start to finish.

The interpreter starts at the top of a python file. It then proceeds line by
line down. For each line it executes the code that is in the gloabl or higher level (0 indent).

Note that functions are treated differently. The function objects are created
and bound to their names, but the code block isn't executed until called.

Note this is why Errors in functions only appear at runtime.

Environment
===========

During runtime the interpreter creates, updates, and deletes frame & namespace objects as part of maintaining the environment. These objects combine to determine what is in scope at a particular point of execution.

Some definitions:
* A namespace is a mapping from names to objects.
* A frame is an execution environment.
* Scope defines what names the interpreter can find given which frame its in and
the namespaces associated.

You are exposed to frame objects when you see error messages. You have
interacted with namesspace objects since the start of this course without
knowing it. Every assignment has added a name to a Namespace object and
associated it with the object instance it references.

When the interpreter encounters a name, it searches in the various namespaces
available to it as specified in the frame. If it is found, the name resolves to
the object it references. If not it springs a `NameError`.

Namespaces & functions
======================

The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.

A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.


Visualising execution
=====================

It is very helpful to maintain a visualisation of what is happening.

Here are some tools to aid with developing that:

http://www.pythontutor.com/visualize.html#mode=edit

http://pyalgoviz.appspot.com/


pdb
===

pdb is the python debugger. Debugging is a way of interacting with a program by freezing execution at a particular point in time, stepping through it, and examining objects.

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


Tip:

Whenever you get an exeception drop a `import pdb; pdb.set_trace()` on the line
before your program terminated. That way you can inspect what went wrong at
that point in time.

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

    python3 -m pdb my.py

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

Copy the same code into www.pythontutor.com.

After stepping through a few times you will get something like this:

.. image:: /images/inc_visualisation.png

Step through each line of code keeping the visualiser tool and pdb in sync. Use
the visualiser as a map to find the various parts through pdb.

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

Enter `import pdb; pdb.set_trace()` at the beginning of a koan that caused you
difficulty. Step through the execution of the code. When you are done type `c`
to resume execution.

References
==========

There is a lot of complexity here. Only approach if feeling brave and happy for
it to make sense over time.

https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
https://docs.python.org/3.3/reference/executionmodel.html
