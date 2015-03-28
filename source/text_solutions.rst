Text Solutions
**************

`bar.py`
========

.. code-block:: python

    age = input("Enter your age ")
    age = int(age)
    if age < 18:
        print('Underaged'):
    else:
        print('ok')


`ride.py`
=========

.. code-block:: python

    height = input("Enter your height ")
    height = int(height)
    heigth = 200
    if height < 150:
        print('Not tall enough'):
    else:
        print('ok')

`trader.py`
===========

.. code-block:: python

    acme = input("Enter ACME stock price ")
    acme = float(acme)
    if acme < 0.002:
        print('Sell'):
    elif acme > 0.005:
        print('Buy')
    else:
        print('Hold')


`big_corp.py`
=============

.. code-block:: python
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    gender = input("Enter your gender m for male, f for female: ")
    if gender != 'm' or gender != 'f':
        print('Gender must be m or f')

    if gender == 'm':
        print('Hi Mr ' + last_name '. The sale this week is for boxer shorts')
    if gender == 'f':
        print('Hi Ms ' + last_name '. Buy some great lipstick when next in
        store')


`mobile.py`
===========

.. code-block:: python

    phone = input("Enter phone number: ")

    if '0845' in phone:
        print('Charging')
    else:
        print('Free')


`dna.py`
========

.. code-block:: python
    
    dna = ATTGCGCCTTATGCTTAACC
    new = input("Enter DNA strand: ")

    if new in dna:
        print('Found')
    else:
        print('Not Found')

