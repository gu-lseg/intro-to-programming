Solutions to Practicals
***********************

loan.py
=======

.. code-block:: python

    while balance > 0:
        compound_interest = 0.1 * balance
        print('balance: ' + str(balance))
        balance = balance + compound_interest - 20

    balance: 100.0
    balance: 90.0
    balance: 79.0
    balance: 66.9
    balance: 53.59
    balance: 38.949000000000005
    balance: 22.843900000000005
    balance: 5.128290000000007


`turtle_joypad.py`
==================

.. code-block:: python

    import turtle

    tess = turtle.Turtle()

    while True:

        move = input('Type a w d s for left right up down\nType q to exit\n')

        if move == 'a':
            tess.setheading(180)  # west
            tess.forward(10)
        elif move == 'w':
            tess.setheading(90)   # north
            tess.forward(10)
        elif move == 'd':
            tess.setheading(0)    # west
            tess.forward(10)
        elif move == 's':
            tess.setheading(270)  # south
            tess.forward(10)
        elif move == 'q':
            break


bmi_django.py
=============

.. code-block:: python

    from django.shortcuts import render
    from django.http import HttpResponse

    bmi_html = """
    <html>
    <head></head>
    <body>
        <h1>BMI calculator</h1>
        <p>Your bmi is {}</p>
        <p>see where you are on this chart:</p>
        <img src="http://upload.wikimedia.org/wikipedia/commons/e/e9/Body_mass_index_chart.svg">
    </body>
    </html>
    """

    def bmi(request):

        mass = request.GET['mass']
        height = request.GET['height']

        bmi = float(mass) / float(height)**2

        response = bmi_html.format(bmi)

        return HttpResponse(response)


