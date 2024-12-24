#HEAPS
#Mainly used to implement a priority queue

import heapq

nums = [1,1,2,3,1,4,5]
heapq.heapify(nums) #converts a list or any iteerable into a heap or priority queue

#heappush(heap, ele): This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.
#heappop(heap): This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.#
heapq.heappush(nums, 0)
print(nums)  # Output: [0, 2, 1, 5, 4, 3]
smallest = heapq.heappop(nums)
print(smallest)  # Output: 0
print(nums)      # Output: [1, 2, 3, 5, 4]

#Replace the smallest element with a new value and adjust the heap:
heapq.heapreplace(nums, 6)
print(nums)  # Output: [2, 4, 3, 5, 6]


#Python’s heapq module only supports a min-heap. 
# To create a max-heap, you can invert the values by multiplying them by -1 when inserting or removing elements.

#You can use heapq to efficiently find the smallest or largest elements in a list.
#using nsmallest and nlargest
nums = [7, 10, 4, 3, 20, 15]
k = 3
print(heapq.nsmallest(k, nums))  # Output: [3, 4, 7]
print(heapq.nlargest(k, nums))  # Output: [20, 15, 10]


#Efficiently merge multiple sorted lists into a single sorted list using heapq.merge
a = [1, 3, 5]
b = [2, 4, 6]
print(list(heapq.merge(a, b)))  # Output: [1, 2, 3, 4, 5, 6]

#summary
"""

heapq.heapify(list) makes a list a min-heap based on priority values --O(N)
    heapq.heapify(nums)
heapq.heappush(nums, ele) pushes the element to the heap nums O(log N)
    nums = [1, 2, 3]
    heapq.heappush(nums, 0)
    print(nums)  # Output: [0, 1, 3, 2]
heapq.heappop() removes the smallest element from heap O(log N)
    nums = [1, 2, 3]
    heapq.heapify(nums)
    smallest = heapq.heappop(nums)
    print(smallest)  # Output: 1
    print(nums)      # Output: [2, 3]
heapq.heapreplace(nums, ele) Pop and return smallest, and push ele onto the heap  O(log N)
    heapq.heapreplace(nums, 4)
heapq.nsmallest(k, list) Return the k smallest elements O(log N)
    nums = [7, 10, 4, 3, 20, 15]
    k_smallest = heapq.nsmallest(3, nums)
    print(k_smallest)  # Output: [3, 4, 7]
heapq.nlargest(k, list) Return the k largest elements O(k log N)
    nums = [7, 10, 4, 3, 20, 15]
    k_largest = heapq.nlargest(3, nums)
    print(k_largest)  # Output: [20, 15, 10]
heapq.merge(sortedlist1, sortedlist2) Efficiently merge multiple sorted lists into a single sorted list O(k log N)
    a = [1, 3, 5]
    b = [2, 4, 6]
    merged = list(heapq.merge(a, b))
    print(merged)  # Output: [1, 2, 3, 4, 5, 6]




"""

    
