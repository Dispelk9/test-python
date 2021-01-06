#===========================================================
#       P Y T H O N S          H A N D B O O K
#===========================================================

# # how to input string
# value = input("Please enter a string:\n")
 
# print(f'You entered {value}')

# # checking if the value integer float or string

# user_input = input("Enter your Age ")

# print("\n")
# try:
#     val = int(user_input)
#     print("Input is an integer number. Number = ", val)
# except ValueError:
#     try:
#         val = float(user_input)
#         print("Input is a float  number. Number = ", val)
#     except ValueError:
#         print("No.. input is not a number. It's a string")


# # checking datetime from a input

# import datetime

# inputDate = input("Enter the date in format 'dd/mm/yy' : ")

# day,month,year = inputDate.split('/')

# isValidDate = True
# try :
#     datetime.datetime(int(year),int(month),int(day))
# except ValueError :
#     isValidDate = False

# if(isValidDate) :
#     print ("Input date is valid ..")
# else :
#     print ("Input date is not valid..")

# print(datetime.datetime.now())

# Get data from .log file

# import re

# target = r'/* BUG:'
# bugs = []
# with open('logfile.txt', 'r') as infile, open('output.txt', 'w') as outfile:
#     # loop through logfile
#     for line in infile:
#         if line.startswith(target):
#             # add line to bug list and strip newlines
#             bugs.append(line.strip())
#             # or just do regex parsing here
#             # create match pattern groups with parentheses, escape literal parentheses with '\'
#             match = re.search(r'NamedIndividual\(([\w#]+)\)]\),DataHasValue\(DataProperty\(([\w#]+)\),\^\^\(([\w#]+),', line)
#             # if matches are found
#             if match:
#                 # loop through match groups, write to output
#                 for group in match.groups():
#                     outfile.write('{} '.format(group))
#                 outfile.write('\n')


# # L O O P 

# # calculate PT b2
# import math

# loo = input("Input loop: \n")


# for x in range(int(loo)):                           #For Python syntax
#     a = int(input("Input a: \n"))                   #convert string to int
#     b = int(input("Input b: \n"))
#     c = int(input("Input c: \n"))
#     d = (-b + (math.sqrt(b**2 - 4*a*c)))/(2*a)      # square root need math library
#     e = (-b - (math.sqrt(b**2 - 4*a*c)))/(2*a)      
#     print("the result is %s and %s" % (d,e))        # print multiple variables

# print('What is your age?')                            # ask for their age
# myAge = input()
# # print only with string variable, have to convert them into string
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')    

# #if elseif
# name = None                                           # Assign a none variable   
# age  = None
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')
#     age = age + 1                                     # instead age++ we need this


# name = ''                                               # While Python syntax
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
#     if name = 'your name'
#         break                                           # break Python
# print('Thank you!')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#      continue                                             # Continue if true, if not then the latter can not be processed.
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#      break
# print('Access granted.')

# # note: continue and break only in while and for


# # F U N C T I O N
# import random
# def getAnswer(answerNumber):                               # def is used to define a function  
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

# def spam(divideBy):
#     try:                                             # Try clause runs the code, if it gets error, go to except clause
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


# # L I S T
# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[-1]) 	                                 # get the variable at the end of the list
# print(spam[0])                                          
# print(spam[1:3])                                     # S L I C E 


# # Augmented Assignments
# spam = spam + 1 # spam += 1
# spam = spam - 1 # spam -= 1
# spam = spam * 1 # spam *= 1
# spam = spam / 1 # spam /= 1
# spam = spam % 1 # spam %= 1

# # D I C T I O N A R Y
# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}             # size, color, dispostition are data types

# # dictionary can be used like this
# birthdays = {'A':'11-10','B':'15-12','C':'28-02','D':'19-11','E':'18-05'}

# print(birthdays.keys())                                                       # keys() get all information A,B,C,D,E   
# print(birthdays.values())                                                     # values() get all the birthdays           
# print(birthdays.get('A',0))                                                   # get to extract the informations

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print(' I don\'t have the birthday of ' + name)
#         print(' Please input the birthday date: ')
#         newbd = input()
#         birthdays[name] = newbd 
#         print('birthday updated!')
#         print('Continue?')
#         lc = input()
#         if lc == 'y':
#             continue
#         elif lc == 'n':
#             break
#         else:
#             print('Wrong Input')


import copy 

spam = ['A','B','C','D']
cheese = copy.copy(spam)                             # copy using copy library
cheese[1] = 42                                       # add 42 into space 1 of cheese, list start with 0 so 1 is B
print(spam)
print(cheese)
spam[:2]

print("Press Enter to exit")                         # stop the terminal to close after running the program
input()

# keys() values() items()
