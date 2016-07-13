Text
****

Strings 
=======

Text is represented and manipulated using objects of type `str`.

Creation
--------
::

    >>> "hi"        
    hi
    >>> type("hi")     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object

Methods
-------

Many! Consult the online documentation: |string_methods|

.. |string_methods| raw:: html

    <a href="https://docs.python.org/3.4/library/stdtypes.html#string-methods" target="_blank">https://docs.python.org/3.4/library/stdtypes.html#string-methods</a>

Questions
---------


1. Using the documentation, how would you make a string all capitalized?
2. Given the string `"I like chocolate"`, how would you change the word chocolate to something
   else?
3. What other ways would you want to manipulate a string?
4. Try experimenting with the other methods that exist in the docs. How would you use the each
   of those methods to manipulate a string? Use the interpreter interactively to try them out.

Conversion functions
--------------------

At some point, you might want convert between numbers and text.

You can use the `int` and `float` functions to convert `str` objects into number objects::

    >>> int('3')
    3
    >>> float('3.4')     # constructor can convert from str
    3.4
    >>> str(3)
    '3'                  # note the ''s that indicate a str object
    >>> str(3.4)
    '3.4'

User Input
==========

To make programs interactive use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

When the interpreter meets `input` it:

1. Prints the string message passed as an argument to `input`,
2. Stores any characters typed
3. On `enter` returns the characters as a new String.

Here the new string is assigned to the name `name`.

So if the user types in `John` then enter, a string object of value
'John' is assinged to name.

`if` and `elif`
==============

We can define more complex conditional behaviour by combining if with elif and
else:: 

    >>> x = input("Enter your age: ")    # input returns a str 
    Enter your age: 24
    >>> x = int(x)                       # convert to an int
    >>> if x < 18:
    ...     print('You are a child')
    ... elif x == 18:
    ...     print('You have just turned into an adult')
    ... else:
    ...     print('You are an adult')


Exercises
=========

1. Rewrite the number programs `bar.py`, `ride.py` and `trader.py` to take 
   input from the user. 
   Think of an appropriate question to print to screen to solicit 
   a correct response.

What if the user enters nonsense? There is rarely a program without some form
of validation. This is explored in the next exercise.

2. A sign up form on a website for the company 'Very Big Corp. Of America' requires 
   information from its clients. The company wants to do gender based 
   email marketing. Put this code in `big_corp.py`

    a Write a program that asks clients their name, address, and gender. Ensure that 
      gender is represented as either 'm', 'f'. If it is not ask the user again.
      Once all information is inputted print 'Hi Oliver, we have shaving
      blades reduced this week' and for women 'Hi Sarah, we have shampoo currently on sale'

    b The same program now requires people to enter their email address. Add this 
      but ensure it is in the right format. What would a well defined email address look like?
      How can you test that an email address is in the correct format?

3. A mobile phone company bills clients on a certain plan differently depending
   on whether they have dialed a number containing 0845 or not. Write a program 
   that asks the user which number they'd like to dial and answers whether it 
   is 'free' or 'paid'. Use `mobile.py`

4. A geneticist needs your help identifying if a dna sequence exists in
   a larger strand of dna. A DNA sequence consists of a sequence 
   of A, T, G, and Cs. Write a program that takes a DNA sequence from the 
   user and confirms 'Found' or 'Not Found' depending on whether the input 
   is contained in the target DNA strand. Use `dna.py`

   DNA strand: ATTGCGCCTTATGCTTAACC

   As a challenge extend this program to check that the input is correct.

