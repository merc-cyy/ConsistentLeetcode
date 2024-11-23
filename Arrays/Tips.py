#RANGE FUNCTION
#1. range(start-INCLUSIVE, stop-EXCLUSIVE, step): Generates numbers from start up to (but not including) stop, incrementing by step. 
# If step is negative, it generates numbers in reverse order.Uses commas, not colons to separate args
#range(1, 10, 2)   # Generates 1, 3, 5, 7, 9
#range(10, 1, -2)  # Generates 10, 8, 6, 4, 2

#2. To loop through indices in a list using the range() function, you can use range(len(your_list))\\

#JOIN FUNCTION
#1. separator.join(iterable)
#separator: The string you want to place between each element of the iterable. This can be any string, such as a comma ",", space " ", or empty string "".
#iterable: An iterable (like a list or tuple) whose elements (MUST BE STRING ELEMENTS) you want to join into a single string.