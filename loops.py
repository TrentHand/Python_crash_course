#basic For Loop in python
magicians = ['alice', 'david', 'houston']
for magician in magicians:
    print(magician)
#adding a sentence and capitalizing the names
    print(magician.title() + ", that was a great trick!")
#the "\n" adds a new line between the statements.  That's why there's a space
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
#removing the indent closes the loop
print("Thank you everyone!  That was a great show!\n")

#the range() function is an easy way to create a list of numbers
for value in range(1, 5):
    print(value)
#i can convert the range directly into a list using the list() function
numbers = list(range(1,6))
print(numbers)
#numbers can be skipped using the third argument in range
even_numbers = list(range(2, 11, 2))
print(even_numbers)
#this is how you get the squares of a list of numbers
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
#this is how to write the above code with a list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
#how to loop through a list and slice out only certain items
print("Here are the first three players in my team: ")
for player in players[:3]:
    print(player.title())
#this is how to copy an entire list
old_players = players[:]
print(old_players)