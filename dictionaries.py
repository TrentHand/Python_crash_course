#dictionaries are way to store key value pairs in python
alien_0 = {'color': 'green', 'points': 5}
#you access them using the bracket notation of the value
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
#adding new key value pairs to an existing dictionary
print(alien_0)#current value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)#new value
#modifying the values in a dictionary
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
#this is how we can set the speed of an alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
    #move the alien to the right.
    #determine how far the alien moves based on it's current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3
    #the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
#deleting a key value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
    #the del command tells python to remove the 'points' key value pair
del alien_0['points']
print(alien_0)

#storing multiple similar objects in a dictionary
    #this is a poll of favorite programming languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
#looping through all the key value pairs in a dictionary
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
#the first item corresponds to the key and the second is the value from the key
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
#getting just the names:
for name in favorite_languages.keys():
    print(name.title())
#accessing the values associated with particular keys
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorit language is " +favorite_languages[name].title() + "!")
#seeing if a name isn't in the list
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")
#using the sorted() method to get the keys back in alphabetical order
for name in sorted(favorite_languages.keys()):
    print("Thank you " + name.title() + " for taking our poll")
#this is how we can just return the values
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
#use "set()" to filter out any duplicate values and only print them once
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())    
#NESTING
#nesting dictionaries into a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#creating a code that will automatically generate 30 aliens
    #make an emply list for storing aliens
aliens = []

    #make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    #show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
    #show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
    #changing some of the aliens to yellow with medium speed
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    #show the first five aliens
for alien in aliens[0:5]:
    print(alien)
print("...")
#using lists inside of dictionaries
    #store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
    #summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the folowing toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
#nesting a list in a dictionary to associate more than one value with a key
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#nesting dictionaries in dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last'] 
    location = user_info['location']
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())










