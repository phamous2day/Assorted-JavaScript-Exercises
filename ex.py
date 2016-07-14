# # print "Hello World!"
# # print "Hello Again"
# # print "I like typing this"
# # print "This is fun"
# print "Yay! Printing"
# EXERCISE 4
#
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
#
# print "there are", cars, "cars available"
# print "there are only", drivers, "drivers available."
# print "there will be", cars_not_driven, "empty cars today"
#
#
# Exercise 5
# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth
#
# # this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight)
#
# Exercise 6
# x = "There are %d types of people" % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s" % (binary, do_not)
#
# print x
# print y
#
# print " I said: %r." %x
# print "I also said: '%s'." %y
#
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"
#
# print joke_evaluation % hilarious
#
# w = "this is the left side of ..."
# e = "a string with a right side."
#
# print w + e
#
#
# # Exercise 7
#
# print "Mary had a little lamb"
# print "Its fleece was white as %s." % 'snow'
# print "And everywhere that Mary went."
# print "." *10 #what'd that do?
#
# end1 = "C"
# end2 = 'h'
# end3 = 'e'
# end4 = 'e'
# end5 = 's'
# end6 = 'e'
# end7 = 'b'
# end8 = 'u'
# end9 = 'r'
# end10 = 'g'
# end11 = 'e'
# end12 = 'r'
#
# #watch that comma at the end. try removing it to see what happens
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 +end11 + end12
#
#
#
#  Exercise 9
#
# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nfeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print "here are teh days: ", days
# print "here are teh months: ", months
#
# print """
# There's something going on here. With the three double-quotes. We'll be able to toype as much as we like. Even 4 lines if we want, or 5 or 6
# """
#
#
# Exercise 10
#
# tabby_cat = "\tI'm tabbed in"
# persian_cat = "I'm split\non a line"
# backlash_cat = "I'm \\a \\ cat"
#
# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* catnip\n\t*Grass
#
# print tabby_cat
# print persian_cant
# print backslash_cat
# print fat_cat
#
#
# Exercise 11
#
# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()
#
# print "So, you're %r old, %r tall and %r heavy." % (
#     age, height, weight)
#
#
# execise 12
#
# age = raw_input("How old are you?")
# height = raw_input("How tall are you?")
# weight = raw_input("How heavy are you?")
#
# print "so, yu're %r old, %r tall and %r heavy" %(age, height, weight)
#
# exercise 13
#
# from sys import argv
#
# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third
#
# python exercise1.py first 2nd 3rd
# The script is called: exercise1.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
#
#
# Exercise 14
#
# from sys import argv
# script, user_name = argv
# prompt = '> '
#
# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s" %user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print """
# alright, you said %r about liking me.
# YOu live in %r. Not sure where that is.
# And you have a %r computer. Noice!!
# """ % (likes, lives, computer)
#
# Exercise 15
# from sys import argv
# script, filename = argv
#
# txt = open(filename)
#
# print "Here's your file %r:" %filename
# print txt.read()
#
# print "Type the filename again:"
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print txt_again.read()
#
# Exercise 16
#
# from sys import argv
#
# script, filename = argv
#
# print "we're going to erase %r" % filename
# print "If you don't want that , hit ctrl-c(^c)"
# print "If you do want that, hit return"
#
# raw_input("?")
#
# print "opening file ..."
# target = open(filename, 'w')
#
# print "Truncating the file. Goodbye!"
# target.truncate()
#
# print "now I'm going to ask you for 3 lines"
#
# line1 = raw_input('Line 1: ')
# line2 = raw_input('line2: ')
# line3 = raw_input('line3: ')
#
# print "I'm going to write these ot the file"
#
# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
#
# print "And we finally, close it"
# target.close
#
#
# ex 17
#
# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print "copying from %s to %s" % (from_file, to_file)
#
# in_file = open(from_file)
# indata = in_file.read()
#
# print "The input file is %d bytes long" % len(indata)
#
# print "Does the output file exist? %r" %exists(to_file)
#
# print "ready, to hit return to contineu, ctrl c to abort"
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "Allright, all done"
#
# out_file.close()
# in_file.close()
#
#
# ex18
# this one is like your scripts with argv
# def print_two(*args):
#     arg1, arg2= args
#     print"arg1: %r, arg2: %r" % (arg1, arg2)
#
# #ok, that *arags is actually pointless, but we can do this:
#
# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# #This just takes one argument
# def print_one(arg1):
#     print "arg1: %r" % arg1
#
# #this takes no arguments
# def print_none():
#     print "I got nothin'."
#
# print_two("Bruce", "Wayne")
# print_two_again("Clark", "Kent 2")
# print_one("First!")
# print_none()
#
# ex19
#
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "you have %d cheeses" %cheese_count
#     print "you have %d boxes of crackers" % boxes_of_crackers
#     print "man that's enough for a party!"
#     print "Get a blanket. \n"
#
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
#
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5+6)
#
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
# ex20
#
# from sys import argv
# script, input_file = argv
#
# def print_all(f):
#     print f.read()
#
# def rewind(f):
#     f.seek(0)
#
# def print_a_line(line_count, f):
#     print line_count, f.readline()
#
# current_file = open(input_file)
#
# print "first let's print the whole file: \n"
#
# print_all(current_file)
#
# print "now let's rewind, kind of like a tape."
#
# rewind(current_file)
#
# print "let's print 3 lines:"
#
# current_line = 1
# print_a_line(current_line, current_file)
#
# current_line = current_line+1
# print_a_line(current_line, current_file)
#
# current_line = current_line+1
# print_a_line(current_line, current_file)
#
# ex21
#
# def add(a,b):
#     print "ADDING %d + %d" %(a,b)
#     return a+b
#
# def subtract(a,b):
#     print "SUBTRACTING %d - %d" %(a,b)
#     return a-b
#
# def multiply(a,b):
#     print "MULTIPLYING %d * %d" %(a,b)
#     return a*b
#
# def divide(a,b):
#     print "DIVIDING %d/%d" %(a,b)
#     return a/b
#
# print "Lets do some math with just functions!"
# age = add(30,5)
# height = subtract(78,4)
# weight = multiply(90,2)
# iq = divide(100,2)
#
# print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)
#
# # A puzzle for the extra credit, type it anyway
#
# print "here is a puzzle."
#
# #Don't think in order of operations, instead it's collecting arguments/parameters first, then performing the operations from inner to outer.
#
# # what = add(age, subtract(height, multiply(weight, divide(iq,2))))
# # m = divide(iq,2)
# # what = add(age, subtract(multiply(weight, m), height))
# variable =subtract(height, weight)
# what = add(variable,weight)
#
# print "That becomes: ", what, "Can you do it by hand?"
#
#
# ex22 (write previous exercises by hand)

#ex23 read python code on github

#ex24

# print "Let's practice everything"
# print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#
# poem= """
# \t The lovely world
# logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """
#
# print "----------"
# print poem
# print "----------"
#
# five = 10-2+3-6
#
# print "this should be five: %s" %five
#
# def secret_formula(started):
#     jelly_beans= started *500
#     jars = jelly_beans/1000
#     crates = jars/100
#     return jelly_beans, jars, crates
#
# start_point = 1000
# beans, jars, crates = secret_formula(start_point)
#
# print "With a starting point of : %d" %start_point
# print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)
#
# start_point = start_point/10
#
# print "We can also do that this way:"
# print "We'd have %d beans, %d jars, and %d crates" %secret_formula(start_point)

#ex25

def break_words(stuff):
    """This function will break words for us. """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words. """
    return sorted(words)

def print_first_word(words):
    """Prints the first word after poppint it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off """
    word = words. pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns teh sorted words. """
    words = break_words(sentence)
    return sorted_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence. """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one. """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
