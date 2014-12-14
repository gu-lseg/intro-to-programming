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

Running the Koans
=================

Setup 
-----

We need to:

* Download zip file from https://github.com/arachnegl/python-koans
* move it from Downloads into your home directory (for me its `C:\Users\greg-lo`)
* unzip it 
* change directory (`cd`) into the python-koans-master directory

Here are the commands::

    C:\Users\greg-lo>move Downloads\python-koans-master .  # 1
    C:\Users\greg-lo>unzip python-koans-master.zip         # 2
    C:\Users\greg-lo>cd python-koans-master                # 3
    C:\Users\greg-lo\python-koans-master>                  # 4

Notes:

1. move the downloaded file into the user directory. `.` represents the users'
   directory.
2. unzip the file.
3. change into the unzipped directory.
4. Note the updated location in the prompt.

Running
-------

Now we are ready to execute the contemplate_koans.py program::

    C:\Users\greg-lo>python contemplate_koans.py about_asserts

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
