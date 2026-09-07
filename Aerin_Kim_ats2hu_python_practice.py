# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 


#Name: Aerin Kim
#Date: 9/6/2026
# Assignment: 01
#Generative AI Statement: This assignment was assisted by ChatGPT-5.6 Luna on September 6, 2026. ChatGPT-5.6 Luna was used to explain the prompt in Problem 1 and to address errors in importing the library for Problem 3.


# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7


""" # you can use three double-quotes to write multi-line comments

INPUT integer value N

SET a equal to zero (a = 0)
SET b equal to one (b = 1)
SET count equal to zero (count = 0)
SET total equal to zero (total = 0)

WHILE count is less than N:
    ADD integer value a to current total

    SET next_value equal to sum of a and b 

    SET a equal to b 
    SET b equal to next_value 

    ADD one to count
OUTPUT total


"""


# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).


N = 6 # integer value N indicating how many fibonacci values to sum (should sum to 12)

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # track how many fibonacci numbers have been added to total
total = 0 # hold  the sum of the running total of fibonacci numbers

# loops through the first 6 values of the fibonacci sequence and adds them to total (e.g. i = 0,1,2,3,4,5)
while count < N:
    # add the current fibonacci number to the total
    total = total + a # ERROR: should add a to total, not b. The first fibonacci number is a, not b.

    # move to the next fibonacci number in the sequence
    next_value = a + b

    # adjust positions of a and b to move to the next fibonacci number in the sequence
    a = b
    b = next_value

    # increase count by 1 to track how many fibonacci numbers have been added to total
    count = count + 1

print(total)


# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.


import numpy as np

fibonacci_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

standard_deviation = np.std(fibonacci_seq) # use numpy's std function to calculate the standard deviation of the fibonacci sequence

print(standard_deviation)


# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.


# function using same process as in Problem 2 to calculate the sum of the first N fibonacci numbers
def summed_sequence(N):
    a = 0
    b = 1
    total = 0
    count = 0

  
    while count < N:
        total = total + a

        next_value = a + b

        a = b
        b = next_value

    return total


N_values = [5, 10, 15, 20, 25, 30] # list of N values to calculate the sum of the first N fibonacci numbers
sums = [] # list to store the sums of the first N fibonacci numbers

for N in N_values: # goes through each item in the N_values list
    sums.append(summed_sequence(N)) # calculates the sum of the each of the N fibonacci numbers using the summed_sequence function and adds it to empy list sums

print(sums)


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # cannot compare str to int value (TypeError); change from str to int value
    b = 1 # cannot add str to int value (TypeError); change from str to int value
    index = 0 # using index before it is defined (NameError); define index before using it

    while a <= limit: # compares string value of a to integer value of limit (TypeError)
        next_value = a + b
        a = b
        b = next_value
        index += 1 # using index before it is defined (NameError)

    return index


result = find_fib_above_limit(50) # value of limit is an integer
print("The index of the first number above your limit is: ", result)


# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit): # prompt asks for the sum of all odd Fibonacci numbers not even Fibonacci numbers, so change the function name to sum_odd_fib
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # this line checks if the Fibonacci number is even-->change to check for odd value (using !=)
            total += b  # this line should add the odd Fibonacci number to the total, not set total equal to b
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_odd_fib(1))
print(sum_odd_fib(2))    
print(sum_odd_fib(3))    
print(sum_odd_fib(5))   
print(sum_odd_fib(10))   
print(sum_odd_fib(20))  
# %%
