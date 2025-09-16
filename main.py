"""# working with numbers
from pyscript import display, document


def getting_data(e): # creating = fuction
    document.getElementById('output').innerHTML = " "
    username = document.getElementById('username').value # getting the data from an input field
    password = document.getElementById('password').value

    display(f'Your username is {username} and your password is {password}. Do you confirm?', target='output')
"""
# 1 using arithmetic operatios
from pyscript import display, document


def trapezoid_area(e):
    base1 = float(document.getElementById('base1').value)
    base2 = float(document.getElementById('base2').value)
    height = float(document.getElementById('height').value)
    area = ((base1 + base2 / 2 ))* height

    display(f'The area of a trapezoid with {base1} and {base2} divided by {height} times is {area}', target='output')