# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:06:58 2017

@author: ammara
"""

#Chapter 3
##################################################################             
#Exercise 3.1.
# Write a function named right_justify that takes a string named s as a parameter
#and prints the string with enough leading spaces so that the last letter of the string is in column 70
#of the display.



# Solution 1 Short cut
def right_justify(s):
    print (' '*(10)+s)

right_justify('allen') 
                
# Solution 2 Long way
def right_justify(s):
    curr_len=len(s)
    final_len=70
    while curr_len<final_len:
        curr_len=curr_len+1 
    print(' '*(curr_len)+s) #pay attention to indexing of print
        
right_justify('monty')

############################################################################################
#caveas for 
#1
 #if you put print right below curr_len then it will print your string 70 times,
 #each time with one space movement, but we need only one final output 

#2 make sure to put space between two commas on "print" line e.g '' will not justify your input
# hence ' '  is coreect   '' is incorrect 

###########################################################################################



#################################################################################
#Exercise 3.2#
#A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
    f()
    f()
#Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
    print('spam')
do_twice(print_spam)


#solution 3.2.1 . Type this example into a script and test it

def do_twice (f): # we have to provide this function with argument which is spams 
    f() 
    f() 

def print_spam():
    print('spam') 

do_twice(print_spam)

#solution 3.2.2  
#Modify do_twice so that it takes two arguments, a function object and a value, and calls the
#function twice, passing the value as an argument.

def do_twice(cot,rib):
    print(cot,rib)
    print(cot,rib)

do_twice('spam',3)

#solution 3.2.3
#Copy the definition of print_twice from earlier in this chapter to your script.

def print_twice(amy):
    print(amy)
    print(amy)

#solution 3.2.4
#Use the modified version of do_twice to call print_twice twice, passing 'spam' as an

print_twice('spam')

#solution 3.2.5

#Define a new function called do_four that takes a function object and a value and calls the
#function four times, passing the value as a parameter. 
#There should be only two statements in
#the body of this function, not four.



def do_four(obj,val):
    print(obj*4)
    print(val*4)

do_four('coding ','thesis ')


#alternative solution

def do_four(obj,val):
    do_twice(obj,val)
    do_twice(obj,val)

do_four('coding ','thesis ')


###################################################################
#caveat while calling a function , the input needs to be string
#if it is not defined before.
###################################################################


###################################################################


#Exercise 3.3. Note: This exercise should be done using only the 
#statements and other features we have learned so far.
#1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         | |
| | |
| | |
| | |
+ - - - - + - - - - +
| | |
| | |
| | |
| | |
+ - - - - + - - - - +

def grind_fun(f):
        print('+ ', (4*'- '),'+', (4*' -'),' +')
        for i in range(4):
            print('|           '*3)
        print('+ ', (4*'- '),'+', (4*' -'),' +')
        for i in range(4):
            print('|           '*3)
        print('+ ', (4*'- '),'+', (4*' -'),' +')
    
grind_fun('f')  

#################################################################################



def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end='')

def print_post():
    print('|        ', end='')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_twice(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()










