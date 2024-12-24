#Dicts
new = {}
new[key] = value
print(new.get(key))#value
ans = new.get(key) #print(ans) == value
new.pop(key)#removes key-value pair

new.keys() #return list of keys
new.values() #return list of values
new.items() #return list of key value pairs
new.copy() #returns a copy of dict

#SETS
myset = {"apple", "banana", "cherry"} 
myset2 = set(("apple", "banana", "cherry")) #note the double round brackets
#Sets are unordered, so you cannot be sure in which order the items will appear hence cannot be referred to by index or key.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#Duplicate values will be ignored:
#The values True and 1 are considered the same value in sets, and are treated as duplicates:

len(myset) #returns length of the set
for i in myset:
    print(i) #can iterate through the set
myset.add("cow") #add items to set

#To add items from any list/set/dict into the current set, use the update() method.
myset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
myset.update(mylist)

myset.remove("cow") #remove item but raises an error if value doesn't exist
myset.discard("cow") #remove item but raises no error if value doesn't exist
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
myset.clear() #empties the set
del myset #deletes set completely
"""
Sets are implemented as HashTables so their functions are O(1)
"""

##
#The union() method returns a NEW set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # OR set1 | set2 #OR set1.union(set2, set3, set4) #OR set1 | set2 | set3 |set4 #OR 
print(set3)
#The union() method allows you to join a set with other data types, like lists or tuples.The result will be a set.
#The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
#Both union() and update() will exclude any duplicate items.


#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #OR set1 & set2 #OR 
print(set3)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #OR set1 - set2 
print(set3)

#The difference_update() -= method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #OR set1 ^ set2 
print(set3)
#The symmetric_difference_update() ^= method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

#isdisjoint()	 	Returns whether two sets have a intersection or not
#issubset() returns whether THIS SET is contained in another set
#issuperset() returns whether this set IS CONTAINED in another set


#HASHTABLES
#A hash table is the general concept or data structure.
#A hash map is a practical implementation of a hash table in programming languages

#Yes, in Python, you can use a dictionary (dict) as a hash table. 
# Python's dictionary is implemented as a highly optimized hash table under the hood and is designed for fast lookups, insertions, and deletions.





