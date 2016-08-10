Appendix A: Mac OSX
*******************

You interact with python using the `terminal` program.

You can find it by looking in the applications > utilities folder.

A shortcut: 

1. Press `Cmd + space` (the two keys together)
2. A search prompt pops up.
3. Type `terminal` and press enter. 

.. _terminal-101:
Terminal 101
================

Typically you interact with your operating system using a mouse with certain
actions: point, click, drag. Using these you can launch programs and move files.

The `terminal` program offers the same interaction but using typed commands:
    
When `terminal` launches you get a prompt:: 

    ~ >

The prompt gives you your current location followed by a `>`. 
Here I am in the directory `COMPLETE THIS` which itself is in the directory `Users`. 

This will list all the files and folders in your current directory.

Here are all the commands you need for this course:

* cd    - change directory
* ls    - list the directory's contents
* cp    - copy a file or a directory
* mv    - move a file or a directory
* mkdir - make a directory
* rm    - delete a file or directory
* unzip - unzip a zipped (compressed) file

.. tip::
    There is nothing here that you aren't familiar doing with the
    mouse. If necessary use your mouse to orientate yourself.

The Python Interpreter
======================

Python is installed on Mac OSX machines by default

::

    PATH>python
    Python 3.4.2 (v3.4.2:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

.. tip::

    At first it is normal to confuse the terminal and the python interpreter.
    Python instructions don't run in the terminal shell and shell commands don't
    work in the interpreter.

    The interpreter has `>>>` as its prompt

    The terminal shell has the file path eg `PATH >`

