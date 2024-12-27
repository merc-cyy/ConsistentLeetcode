"""
Uses Last in First Out algorithm, think of a stack of plates, push to the top and pop from the top
Implemented as a list, from a module

"""

#as a list
new_stack  = []
new_stack.append(1) # pushes 1 to the top of the stack
new_stack.pop() #pops from the stack

#we can also use the collections library to access the deque module 

"""
Implementation using collections.deque:
Python stack can be implemented using the deque class from the collections module. 
Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, 
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
The same methods on deque as seen in the list are used, append() and pop().
 """
from collections import deque
stack = deque()
# append() function to push
10
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack:')
print(stack)

# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)
# uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty
"""

Output
Initial stack:
deque(['a', 'b', 'c'])

Elements popped from stack:
c
b
a

Stack after elements are popped:
deque([])

"""

"""
Implementation using queue module
Queue module also has a LIFO Queue, which is basically a Stack. 
Data is inserted into Queue using the put() function and get() takes data out from the Queue. 
"""
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())