Appendix A: Windows
*******************

You interact with python using the `cmd.exe` program.

You can find it by searching in the start prompt. 

A shortcut: 

1. Press `Windows + R` (the two keys together)
2. A search prompt pops up.
3. Type `cmd.exe` and press enter. 

Command line 101
================

Typically you interact with your operating system using a mouse with certain
actions: point, click, drag. Using these you can launch programs and move files.

The `cmd.exe` program offers the same interaction but using typed commands:
    
When `cmd.exe` launches you get a prompt:: 

    C:\Users\greg-lo>

The prompt gives you your currnent location followed by a `>`. 
Here I am in the directory `greg-lo` which itself is in the directory `Users`. 
`C` refers the hardrive I am on.

Now you enter the `dir` command:: 

    C:\Users\greg-lo> dir

This will list all the files and folders in your current directory.

Here are all the commands you need for this course:

* cd    - change directory
* dir   - list the directory's contents
* copy  - copy a file or a directory
* move  - move a file or a directory
* mkdir - make a directory
* del   - delete a file or directory
* unzip - unzip a zipped (compressed) file

.. tip::
    There is nothing here that you aren't familiar doing with the
    mouse. If necessary use your mouse to orientate yourself.

The Python Interpreter
======================

When you install python in windows it gives you the option to add the
executable (`python.exe`) to your system path. 

Unfortunately we need to specify the full path each time: `\Python34\python.exe`.

::

    C:\Users\greg-lo>python
    Python 3.4.2 (v3.4.2:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

.. tip::

    At first it is normal to confuse the command line and the python interpreter.
    Python instructions don't run in the command shell and shell commands don't
    work in the interpreter.

    The interpreter has `>>>` as its prompt

    The command shell has the file path eg `C:\Users\greg-lo\>`

