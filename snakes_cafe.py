
multi_line = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

"""

order_more = """
***********************************
** What else would you like to order? **
***********************************
"""


order_count = 0
def user_input(order_count):
    if order_count == 0:
        print(multi_line)
        order_count += 1
        selection = input()
        print(f'** {order_count} order of {selection} have been added to your meal **')
        user_input(order_count)
    elif order_count > 0:
        order_count += 1
        print(order_more)
        selection = input()
        print(f'** {order_count} order of {selection} have been added to your meal **')
        user_input(order_count)
    

user_input(order_count)
