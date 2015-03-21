Koans
-----

The koans use the keyword `assert` a lot. When you assert something you are stating
that it must be true.

In python true and false are represented by the keywords True and False.

`assert` passes silently when it is followed by True but throws an Error when followed by False::

    >>> assert True
    >>> assert False
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError
    >>>

In the Koans you have to find answers that evaluate to True for the `assert` to
pass.

Using your intuition try to complete the about_asserts koans.

Visit the appendix on windows for getting started.

::

    C:\Users\greg-lo> python3 contemplate_koans.py about_asserts

.. tip::

    Try copying small lines of code into the python interpreter to experiment 
    interactively with the code. Do this whenever you are stuck.


Run these to explore `int` objects:: 

    python contemplate_koans.py about_integers


Methods that exist on string objects facilitate working with text. We will
explore these by running the koans::

    python contemplate_koans.py about_strings

Conditionals::

    > python contemplate_koans.py about_if_statements
