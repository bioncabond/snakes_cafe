from sys import exit
from food import food

# # Input indicator 
# print(">") 

#Menu Header/Welcome 
print ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

# Menu Sections 

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

""") 

# Set up food objects -> Moved to food.py
# food = [ "Wings",
# "Cookies",
# "Spring Rolls",
# "Salmon",
# "Steak",
# "Meat Tornado",
# "A Literal Garden",
# "Ice Cream",
# "Cake",
# "Pie",
# "Coffee",
# "Tea",
# "Unicorn Tears"] 
# made an empty array to push stuff into
food_list = [] 
# set up order function 


# print(food.values())

#makes sure that the food type is actually in the list of food
real_food = []
for i in food.values():
    # print(food.values())
    real_food += i
# print(real_food)

def order_food(): 
    order = input(">") 

    if order in real_food:
        # add it to the food list array
        food_list.append(order)
        # now count how many items are in that array
        add=food_list.count(order) 
        for item in food_list:
            if add > 1:  
                print(f'** {add} orders of {item} have been added to your meal **')
                order_food()
            else: 
                print(f'** {add} order of {item} have been added to your meal **')                
                #call back the order_food function & moved the 
                order_food()
    elif order == "end":
        exit()
    else:
        order_food()
        print("***Please make a different menu selection***") 

order_food() 
    