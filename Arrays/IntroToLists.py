#In Python lists and arrays are twodifferent things
#Just use lists, more flexible and mutable
a = [1,2,3,4,5]
#can hold items of many types
# you can create a vector of each character using list() on any tuple or string
a = "apple"  #['a', 'p', 'p', 'l', 'e']
b = (list(a))  #['a', 'p', 'p', 'l', 'e']
m = [1,2,3,4,5]
#INITIALIZATION
c = ["f"] * 7
print(c) #['f', 'f', 'f', 'f', 'f', 'f', 'f']

#INDEXING
print(b[0])#a
print(b[-1]) #e negative indexing starts from the back so it wraps
print(m[2:])#[345]
# k[startidx:endidx_exclusive:step]
# omission of startidx or endidx means from idx 0(start) or to the end of the list(end)
# negative idxing starts at the back so using -3 accesses the third-last, -2 second last and a step value of -1 means reversing stepping

#FUCNTIONS
b.append(12)#adds at the end == ['a', 'p', 'p', 'l', 'e', 12]
print(b)
b.extend([12,13,14])#adds mutliple elements at the end == ['a', 'p', 'p', 'l', 'e', 12, 12, 13, 14]
print(b)
print(b.insert(1,100))#inserts at a specific index == ['a', 100, 'p', 'p', 'l', 'e', 12, 12, 13, 14]-O(n) time
print(b)

#INSERTION V DELETION o(n)
w = [1,2,3,4,5]#Insertion v updating
w[0] = "g"
print(w)#['g', 2, 3, 4, 5]
#w[5] = "h" OUT OF BOUNDS INDEX. Just append
w.remove(2)#removes the first occurrence of a value
print(w)#['g', 3, 4, 5] 
w.pop() # pop()removes the item at that index or if no arg, removes last element
w.pop(0)#returns reoved element
#w.pop(5) OUT OF RANGE
del w[0]#delete element at that index returns none
print(w)#[4]


#ITERATION
a = [1,2,3,4,5]
f = []
# for i in a:### WRONG!!  A for i in a means i takes the value itself not index
#     a[i] = a[i] * 2
#     f.append(a[i])
# print(f) 
#CORRECT
for i in a:
    i = i * 2
    f.append(i)
print(f) 

#Iterate over indices
for i in range(len(a)):#range(len(a)) generates a sequence of indices from 0 to len(a) - 1, which you can use to access each element by index.
    i = i * 2
    f.append(i)

#Iterate over index and value
for index, element in enumerate(a):#enumerate(a) returns pairs of (index, element) for each item in a, so you can directly access both the index and the element.
    element = element * 2
    f.append(element)



#MATRICES
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]#List of lists
# Access element at row 2, column 3
print(matrix[1][2]) 


#LIST METHODS
a = [1,2,3,4,5]
a.append(34)#add to end of list o(1)
a.copy() #returns a shallow copy. o(n)
 #In short, with a shallow copy, the outer list is duplicated, but any nested (inner) elements are still shared between the original and copied lists.(reference same inner elements.
a.clear()# removes all elements forma list o(n)
a = [1,2,3,3,3,4,5,5]
a.count(3) #returns the Count of the occurrences of a specified element(not index) in a list 0(N)
a.index(5)#returns index of first occurrence of specified elemento(n)
print(a)
a.reverse()#reverses order in a list 0(n)
print(a)
a.sort()#arranges my_list in ascending order. The list is modified directly, so the elements are permanently rearranged. o(nlogn)
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort(reverse=True)#reverse: Optional boolean parameter. If True, the list is sorted in descending order.
print(my_list)  # Output: [9, 6, 5, 5, 2, 1]
#sorted() is a built-in Python function that returns a new sorted list without modifying the original.
#Some LeetCode questions explicitly mention restrictions, such as "without using built-in functions" or "implement your own solution". 
#If this is the case, you’ll need to implement the logic manually rather than using built-in methods.




#LIST SLICING
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[:]#returns the whole list

#list[start:end:STEP]TEMPLATE
# Get elements starting from index 2(start index)
# to the end of the list
b = a[2:]
print(b)
# Get elements starting from index 0 
# to index 3 (excluding 3th index)
c = a[:3]
print(c)
# Get elements from index 1 (start-inclusive)
# to index 4 (excluding index 4)(end-exclusive)
b = a[1:4]
print(b)

#Negative indexing is useful for accessing elements from the end of the list. 
#The last element has an index of -1, the second last element -2, and so on.
# Get elements starting from index -2
# to end of list
d= a[-2:]
print(d)#[8, 9]
# Get elements starting from index 0 
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)#[1, 2, 3, 4, 5, 6]
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)#[6, 7, 8]
# Get every 2nd elements from index -8
# to -1 (excluding index -1)
e = a[-8:-1:2]
print(e)#[2, 4, 6, 8]

#REVERSING A LIST
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get the entire list using negative step
b = a[::-1]
print(b)
# Explanation: The negative step (-1) indicates that Python should traverse the list in reverse order, starting from the end. 
# The slice a[::-1] starts from the end of the list and moves to the beginning which result in reversing list. 
# It’s a quick and easy way to get the list in reverse without changing the original list.





#UNDER THE HOOD
#Yes, exactly! Python lists are implemented as dynamic arrays, which adjust their size automatically as needed. Here’s how they work under the hood:

# How Python Lists Expand: Dynamic Array Behavior
# Dynamic Resizing with Doubling:
# When you use append() to add elements to a Python list, the list automatically resizes when it reaches capacity.
# Python lists do this by doubling their capacity when they run out of space. This means that each time the list’s current capacity is filled, a larger block of memory is allocated (usually double the previous size), and all elements are copied into this new space.
# Why Doubling?

# Doubling the size minimizes the number of resizing operations needed as the list grows.
# This approach provides an amortized O(1) time complexity for append() operations, meaning that while individual resizing operations are costly (O(n)), they happen infrequently enough that the average time per append() remains constant.
# Memory Efficiency:

# By allocating extra space in advance, Python lists avoid the need to resize every time a new element is added. This trade-off allows for efficient appending while keeping the list close to the ideal size most of the time.
# List Shrinking:

# Python lists don’t automatically shrink when items are removed, as resizing dynamically could slow down performance. However, the del statement or clear() can free up memory by removing elements.





#LIST COMPREHENSION
#Template: [expression for item in iterable if condition]
a = [1, 2, 3, 4, 5]

res = [val * 2 for val in a]

print(res)
