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


References
==========

There is a lot of complexity here. Only approach if feeling brave and happy for
it to make sense over time.

https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
https://docs.python.org/3.3/reference/executionmodel.html
