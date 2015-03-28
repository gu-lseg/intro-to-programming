Koans (Optional)
****************

Koans are puzzles or exercises that are a great way to reinforce your learnings 
of a programming language's constructs.

Find instructions on how to download and run them below.


Making assertions
=================

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


Visit the appendix on windows for getting started.

Using your intuition try to complete the about_asserts koans.

Making Assertions::

    C:\Users\greg-lo> python3 contemplate_koans.py about_asserts


The Koans
=========

.. tip::

    When confused by code, break it up and use the interactive interpreter 
    to experiment. Formulate assumptions and test them.

Integers:: 

    C:\Users\greg-lo> python3 contemplate_koans.py about_integers

Strings::

    C:\Users\greg-lo> python3 contemplate_koans.py about_strings
    C:\Users\greg-lo> python3 contemplate_koans.py about_string_manipulation

Conditionals::

    C:\Users\greg-lo> python3 contemplate_koans.py about_if_statements

Functions::

    C:\Users\greg-lo> python3 contemplate_koans.py about_functions

Data Structures::
 
    C:\Users\greg-lo> python3 contemplate_koans.py about_lists
    C:\Users\greg-lo> python3 contemplate_koans.py about_dictionaries

Loops::

    C:\Users\greg-lo> python3 contemplate_koans.py about_loops


Instructions
============

Setup 
-----

We need to:

1. Download the `koans zip file`_.
2. Unzip it 
3. Move the unzipped folder from Downloads 
   to your home directory (for me its `C:\Users\greg-lo`)

.. _koans zip file: https://github.com/arachnegl/python-koans/archive/master.zip

Now open `cmd.exe`::

    C:\Users\greg-lo> 

Change directory (`cd`) into the python-koans-master directory::

    C:\Users\greg-lo> cd python-koans-master
    C:\Users\greg-lo\python-koans-master> 

Note the updated location in the prompt.

You are setup!

Running
-------

You run the koans by calling the `python3` interpreter on the
`contemplate_koans.py` file followed by a name such as `about_asserts`::

Now we are ready to execute the contemplate_koans.py program::

    C:\Users\greg-lo> python contemplate_koans.py about_asserts

The above instruction is understood as calling the python program and passing in two parameters: a file name 'contenplate_koans.py' and some text 'about_asserts'.

The output should be similar to this::

    Thinking AboutAsserts
      test_assert_truth has damaged your karma.

    You have not yet reached enlightenment ...
      AssertionError: 0 is not true

    Please meditate on the following code:
      File "/Users/greg/TEACHING/python_koans/koans/about_asserts.py", line 13, in test_assert_truth
        assert False  # replace with True


    You have completed 0 koans and 0 lessons.
    You are now 77 koans and 9 lessons away from reaching enlightenment.

Note the section that asks you to mediate on a file with a line number.

Answering
---------

Open this file in SublimeText. Find SublimeText in the Start search prompt.

Open the file as specified by the output of `contemplate_koans`. In the above
case:

* open `C:\Users\greg-lo\python-koans-master\koans\about_asserts.py`
* Go to line 13 and replace `False` with `True`. 
* Save the file. 
* Rerun the Koans     

You should find that one line has gone Green and you now have a new challenge.

.. tip::

    Arrange the windows on your screen so that you have your text editor on one
    side and two `cmd.exe`s on the right one above the other. 
    
    Have the command prompt open in one for running the koans.

    Have the python interpreter in the other for experimenting with code.
