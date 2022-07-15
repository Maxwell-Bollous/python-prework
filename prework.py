# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    """Display a hello message for an entered username"""
    print(f"hello_{user_name.upper()}!")

hello_name('maxwell')



# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    """Display all odd numbers between 1-100"""
    for number in range(1, 101):
        if number % 2 == 1:
            print(number)
        else:
            continue

first_odds()



# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Display the maximum number of a given list"""
    print(max(a_list))

numbers = [18, 112, 229, 945, 156, 462]
max_num_in_list(numbers)



# Question 4:
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Display whether a given year is a leap year"""
    if a_year % 4 == 0:
        print(True)
    else:
        print(False)

is_leap_year(2000)



# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    """Display whether a list is consecutive or not"""
    return print(sorted(a_list) == list(range(min(a_list), max(a_list) + 1)))

number_list = [1, 2, 3, 4, 5, 6]
is_consecutive(number_list)