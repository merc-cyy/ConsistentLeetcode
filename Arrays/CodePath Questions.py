#QUESTION ONE
# Write a function flip_sign() that takes in a list of integers lst as a parameter and 
# returns a new list where each number in the original list has been multiplied by -1.
#input: list of int
#output: list of int
# task: multiply each number by -1

def flip_sign(lst):
    ans = []
    for i in lst:
        ans.append(i * -1)
    return ans

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)


#QUESTION TWO
# Write a function max_difference() that takes in a list of integers lst and 
# returns the difference between the smallest and largest value in the list.
#input: list of int
#output: int
#cqs: natural ints? will type args always be ints? 
#task: diff between smallest and largest value in list
#steps: find largest, find smallest, get diff
def max_difference(lst):#Tiem is 0(N), S- o(1)
    small = lst[0]
    largest = lst[0]#set to be the first in the list

    for i in lst:
        if i > largest:#could also use max(lst) 
            largest = i
        if i < small:#or min(lst)
            small = i
    
    diff = largest - small
    return diff
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)


#QUESTION THREE
#Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).
#Input: none
#OUtput; print out multiples of 5
#Task: find multiple sof 5 between 1 and 100 and print them out
def multiples_of_five():
    for i in range(5,101,5):
        print(i)


#QUESTION FOUR
#Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.
#A divisor of n is any integer d that divides n without leaving a remainder (i.e., n % d == 0).
#input: int n
#output: list of int that a divisors of n
#task: find all numbers that divides n without a remainder
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):  # Check each number from 1 to n
        if n % i == 0:         # If i divides n without a remainder
            divisors.append(i)  # Add i to the list of divisors
    return divisors

#QUESTION FIVE
#Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number
#Input: int n
#OUtput; pritn out all number from 1 - n, except if multiple fo 3 thenprint fizz, and if multiple of 5 print buzz
#Task: loop through all numbers 1-n, check if multiples and print relevant words
def fizzbuzz(n):
    for i in range(1,n):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)


#QUESTION SIX
#Write a function find_missing() that takes in a list nums containing n unique numbers in the range [0,n]. 
# The function returns the only number in the range that is missing from the list.
#Input: list of int
#Output: int, the number not found in the list
#Task:find number missign in that range
#Ideas: 1. for each i in the rnage, check if it exists- o(n2)
#       2. Sort the list, then check through to see what is missign through a while loop
# def find_missing(lst):
#     lst.sort()#ascending order

#     for i in range(len(lst)):
#        next_val = lst[i+1]
#        if next_val is not lst[i] + 1:
#            break
#     return next_val
#BEST: FIND EXPECTED SUM OF VALUES UPTO N THEN GET DIFF WITH WHAT YOU HAVE.
def find_missing(lst):#o(n) takes linear time to get sum of the list
    n = len(lst)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(lst)
    diff = expected_sum - actual_sum
    return diff


#QUESTION SEVEN
#Write a function list_to_number() that takes in a list digits where each item is a digit between 0-9. 
# The function returns the number they represent when combined.
def list_to_number(digits):
    # Convert each digit to a string, join them together, and convert to an integer
    number_str = ''.join(map(str, digits))
    return int(number_str)

#QUESTION EIGHT
#Write a function find_all_occurrences() that takes in a list lst and a value target as parameters 
# and returns a list of all indices where target is found in lst.
def find_all_occurrences(lst, target):
    indices = []
    for index, value in enumerate(lst):
        if value == target:
            indices.append(index)
    return indices







