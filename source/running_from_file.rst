Files & Errors
**************

Files and errors have nothing in common. We're just putting them together.

Running code in a File
======================

We have programmed using the Python interactive shell.

The other way to program uses files. 

We `call` the python program on a file containing python code.

Put the following code into a file:: 

    # A line beginning with '#' is a comment. Python ignores it.

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)
    turtle.exitonclick()  # Why this? Test by commenting it out.

and save the file as `my_turtle_file`.

Now in the console call the python command with the filename as parameter::

    python my_turtle_file.py


This is the more usual way to run programs.


Errors are your guide
=====================

Errors (and Exceptions) are a constant feature of programming.

You have probably already come across this one::

    >>> turtle.forward.
      File "<stdin>", line 1
        turtle.forward.
                      ^
    SyntaxError: invalid syntax
    >>>

Always read them as always tell you what when wrong. They don't always tell you
why things went wrong though. Instead in those cases they act as a clue.

As programmers we learn to read them. Combined with our
intuition we always eventually arrive at solutions.

Often we Google errors.
