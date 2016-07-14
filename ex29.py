# people = 20
# cats = 30
# dogs = 15
#
# if people <cats:
#     print "Too many cats! The world is doomed!"
#
# if people> cats:
#     print "Not many cats! The world is saved!"
#
# if people <dogs:
#     print "The world is drolled on!"
#
# if people > dogs:
#     print "The world is dry!"
#
# dogs +=5
#
# if people >= dogs:
#     print "People are greater than or equal to dogs."
#
# if people <=dogs:
#     print "People are less than or equal to dogs."
#
# if people == dogs:
#     print "People are dogs"

#ex 30

# people = 30
# cars = 40
# trucks = 15
#
# if cars > people:
#     print "We should take the cars"
# elif cars < people:
#     print "We should not take the cars."
# else:
#     print "We can't decide"
#
#
# if trucks > cars:
#     print "That's too many trucks"
# elif trucks < cars:
#     print "Maybe we could take the trucks"
# else:
#     print "We still can't decide"
#
# if people > trucks:
#     print "Alirght, let's just take the trucks"
# else:
#     print "Find let's stay homea again"

#ex31

# print " You enter a dark room with two doors. Do you go through door 1 or door 2?"
#
# door = raw_input("> ")
#
# if door =="1":
#     print "There's a giant bear here eating a cheesecake. What do you do?"
#     print "1: take the cake"
#     print "2: scream at the bear"
#
#     bear = raw_input("> ")
#
#     if bear == "1":
#         print "The bear eats your face of, good job!"
#     if bear == "2":
#         print "The bear eats your legs off, good job!"
#     else:
#         print "well, doing %s is probably better. Bear runs away" % bear
#
# elif door == "2":
#     print "you stare into the endless abyss at Cthulu's retina"
#     print "1.Blueberries"
#     print "2. Yellow jacket clothespins"
#     print "3. Understanding revolvers yelling melodies"
#
#     insanity = raw_input('> ')
#
#     if insanity == "1" or insanity =="2":
#         print "Your body survivies powered by a mind of jello, good job"
#     else:
#         print "the insanity rots your eyes to a pool of muck, good job!"
#
# else:
#     print "You stumble around and fall and a knife and die, good job!"


#ex32

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#
# #this first kind of for-loop goes through a list
# for number in the_count:
#     print "This is the count %d" % number
#
# for fruit in fruits:
#     print "A fruit of type: %s" %fruit
#
# for i in change:
#     print "I got %r" % i
#
# elements = []
#
# for i in range(0, 6):
#     print "Adding %d to the list" %i
#     #append is a function that lists understand
#     elements.append(i)
#
# for i in elements:
#     print "Element was %d" %i


#ex 33

# i = 0
# numbers = []
# while i < 6:
#     print "At the top i is %d" %i
#     numbers.append(i)
#
#     i = i +1
#     print "Numbers now: ", numbers
#     print "At the bottom is %d" %i
#
# print "The numbers: "
#
# for num in numbers:
#     print num

#ex34
# animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
#
#
# 1. The animal at 1 is python
# 2. The third animal (not index 3) is peakcock
# 3. first animal is bear
# 4. animal at index 3 is kanagaroo
# 5. The fifth animal is whale
# 6. animal at index 2 is peacock
# 7. 6th animal is playtypus
# 8.  animal at 4 is whale

#ex 35

# from sys import exit
# def gold_room():
#     print "this room is full of gold. How much do you take?"
#
#     choice = raw_input("> ")
#     if "0" in choice or "1" in choice:
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number")
#
#     if how_much < 50:
#         print "Nice, you're not greedy, you win!"
#         exit(0)
#     else:
#         dead("You greedy bastard!!")
#
# def bear_room():
#     print "There is a bear here"
#     print "the bear has a bunch of honey"
#     print "The fat bear is in front of another door"
#     print "How are you going to move the bear?"
#     bear_moved = False
#
#     while True:
#         choice = raw_input("> ")
#
#         if choice == "take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print "the bear has moved from teh door. You can go through it now."
#             bear_moved = True
#         elif choice == "taught bear" and bear_moved:
#             dead('The bear gets pissed off and chews your leg off')
#         elif choice == "open door" and bear_moved:
#             gold_room()
#         else:
#             print "I got no idea what that means"
#
# def cthulhu_room():
#     print "Here you see the great evil Cthulhu"
#     print "he, it, whatever stares at you and you go insane"
#     print "Do you flee for your life or eat your head?"
#
#     choice = raw_input("> ")
#
#     if "flee" in choice:
#         start()
#     elif "head" in choice:
#         dead("well that was tasty!")
#     else:
#         cthulhu_room()
#
# def dead(why):
#     print why, "Good job!"
#     exit(0)
#
# def start():
#     print "You are in a dark room"
#     print "there is a door to your right and left"
#     print "which door do you take?"
#
#     choice = raw_input(">" )
#
#     if choice == "left":
#         bear_room()
#     elif choice == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve")
#
# start()


#36
