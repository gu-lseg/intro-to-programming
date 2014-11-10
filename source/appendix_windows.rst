Appendix: Windows
*****************

You interact with python using the `cmd.exe` program.

You can find it by searching in the start prompt. 

A shortcut: 

1. Press `Windows + R` (the two keys together)
2. A search prompt pops up.
3. enter `cmd.exe` and select it

Commands
========

Typically you interact with your operating system using a mouse with certain
actions: point, click, drag.

With this you launch programs, move files, do work.

The `cmd.exe` program offers the same interaction but you intreact using
commands that you type.

cmd.exe cheat sheet
-------------------

* exit  - exit cmd.exe
* cd    - change directory
* dir   - list the directory's contents
* copy  - copy a file or a directory
* move  - move a file or a directory
* mkdir - make a directory
* del   - delete a file or directory

Python Interpreter
==================

When you install python in windows it gives you the option to add the
executable (`python.exe`) to your system path. 

Unfortunately we need to specify the full path each time: `\Python34\python.exe`.

::

    C:\Users\greg-lo>\Python34\python.exe
    Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import turtle
    >>> turtle.forward(10)


Koans
=====

Learning takes practice and repetition. Koans are a great way to do this in
programming.

Throughout the course we will make reference to these koans.

Setup 
-----

Python Koans is available on Github:
Steps:

* Download zip from https://github.com/arachnegl/python-koans
* move it from Downloads into your home directory (for me its `C:\Users\greg-lo`)
* unzip it 
* change directory (`cd`) into the python-koans-master directory

Here are the commands::

    C:\Users\greg-lo>move Downloads\python-koans-master .
    C:\Users\greg-lo>unzip python-koans-master.zip
    C:\Users\greg-lo>cd python-koans-master
    C:\Users\greg-lo\ython-koans-master>

Running
-------

Now we are ready to execute the contemplate_koans.py program::

    C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts

    Thinking AboutAsserts
      test_assert_truth has damaged your karma.

    You have not yet reached enlightenment ...
      AssertionError: 0 is not true

    Please meditate on the following code:
      File "/Users/greg/TEACHING/python_koans/koans/about_asserts.py", line 13, in test_assert_truth
        self.assertTrue(_____)  # This should be true


    You have completed 0 koans and 0 lessons.
    You are now 77 koans and 9 lessons away from reaching enlightenment.

Note that you are asked to mediate on a file with a line number.

Answering
---------

Open this file in SublimeText. You can find SublimeText in the Start search prompt.

Open the file as per the output of `contemplate_koans`:
C:\Users\greg-lo\python-koans-master\koans\about_asserts.py

* Go to line 13 and replace `____` with True. 
* Save the file. 
* Rerun the Koans     
     C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts

You should find that one line has gone Green. You now have a new challenge.

.. tip::

    It is often easy to confuse the command shell and the python interpreter.
    Python doesn't run in the command shell and likewise shell commands don't
    work in the interpreter.

    The interpreter has `>>>` as its prompt

    The command shell has the file path eg `C:\Users\greg-lo\>`
