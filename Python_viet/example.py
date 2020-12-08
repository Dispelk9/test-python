#===========================================================
#       M A I L S           S T A T I S T I C S
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


# # calculate PT b2
# import math

# loo = input("Input loop: \n")


# for x in range(int(loo)):                           #for loop syntax
#     a = int(input("Input a: \n"))                   #convert string to int
#     b = int(input("Input b: \n"))
#     c = int(input("Input c: \n"))
#     d = (-b + (math.sqrt(b**2 - 4*a*c)))/(2*a)      # square root need math library
#     e = (-b - (math.sqrt(b**2 - 4*a*c)))/(2*a)      
#     print("the result is %s and %s" % (d,e))        # print multiple variables

print('What is your age?')                            # ask for their age
myAge = input()
# print only with string variable, have to convert them into string
print('You will be ' + str(int(myAge) + 1) + ' in a year.')    

#if elseif
name = None                                           # Assign a none variable   
age  = None
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')




print("Press Enter to exit")                         # stop the terminal to close after running the program
input()

