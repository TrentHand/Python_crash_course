cars = ['audi', 'bmw', 'subaru', 'toyota']
#loops through the cars list and capitalizes the cars, all capsing BMW
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#using the != to check for inequality
topping_choice = 'mushrooms'

if topping_choice != 'anchovies':
    print("hold the anchovies")

#use 'and' to determine if both items return true
age_0 = 19
age_1 = 21
if age_1 >= 18 and age_1 >= 20:
    print("you can drink now!")
else:
    print("sorry, you need a few years")
#use 'or' to determine if one of the items return true

#checking if a certain word is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("mushrooms on your pizza")
if 'pepperoni' in requested_toppings:
    print('pepperoni on your pizza')
else:
    print("sorry, we're vegetarians")

#if-elif-else chain
age = 9
if age < 4:
    print("Your admission cost $0")
elif age < 18:
    print("Your admission is $5")
elif age > 65:
    print("Your admission is $5")
else:
    print("Your admission is $10")

#testing to see if an item is in a list
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple']

requested_toppings = ['mushrooms', 'french fries', 'olives']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza")
