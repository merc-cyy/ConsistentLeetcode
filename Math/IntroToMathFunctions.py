#x is a list#
sum(x) #returns the sum
min(x)
max(x)
round(number, decimal) #Returns a given number rounded to the specified decimal
# Example 1: Round to hundredth
x = 3.14159
rounded = round(x, 2)
print(rounded) # Prints 3.14

s.isalpha() #Returns true if all characters in given string are alphabetic letters (a-z).
s.isalnum() #Returns true if all characters in given string are alphanumeric (a-z or 0-9).
s.find(x) #Returns start index of the first occurrence of substring x in a given string. Returns -1 if x is not in the string.
s.count(x) #Returns the frequency of the substring x in the given string.

"""
Ordered sequences Both strings and lists are ordered sequences of data.
Indexed by Integers Both strings and lists can be indexed using integers (e.g. lst[0] or s[0]).
Slicable Both strings and lists can be sliced to access a subsection of the string/list (e.g. lst[1:3] or s[1:3]).
Iterable Both strings and lists are iterable meaning we can loop over them using a for loop.
Length We can use the len() function to get the length of either a string or list
"""

#The // operator does int division is also known as floor division. x // y returns the result of x divided by y rounded down to the nearest whole integer.
print(5 // 2) # Prints 2 because 5 / 2 = 2.5 which rounded down is 2
print( 6 // 2) #3
#/ does float division
print(7 / 2)   # Output: 3.5
print(6 / 3)   # Output: 2.0


abs(x) #Returns the absolute value of a given number. The absolute value of a number is the distance of that number from 0.

#We can represent positive and negative infinity with the following syntax.
positive_infinity = float('inf')
negative_infinity = float('-inf')