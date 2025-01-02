Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: 
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []


Algorithm 1:
Using two pointers.

We can reverse this list in 0(n) time and O(1) space using two pointers.   
Have a prev, and curr pointer. set the curr to the head and prev to Null(behind the head)
First off, you want to save the curr.next in a value just to not lose the rest of the list after you reverse the link.
Now after saving, you want to set curr.next to prev. This reverses the link in that the current node is set to now point at the prev node.
You have now reversed the link so you advance the pointers and do the same for the next two nodes. 
Move prev to curr, move curr to the temp variable in which you had initially saved.

Test cases:
NORMAL: 1->2->3->4->5->#
prev is null; curr is 1;save curr.next in temp; set curr.next to prev now 1 points at null; move prev to curr and now prev is at 1; move curr to temp
prev is 1, curr is 2; save curr.next to temp; set curr.next to prev and now 2 points to 1; move prev to curr and now prev is at 2; move curr to temp and now curr is at 3
prev is 2, curr is 3; save curr.next to temp(4); set curr.next to prev and now 3 points to 2; move prev to curr now prev is at 3; move curr to temp and now curr is at 4
prev is 3, curr is 4; save curr.next to temp(5); set curr.next to prev and now 4 points to 3; move prev to curr and now prev is at 4; move curr to temp and now curr is at 5
prev is 4, curr is 5; save curr.next to temp(null); set curr.next to prev and now 5 points to 4; move prev to curr and now prev is at 5; move curr to temp and now curr is null
loop exits when curr is null and returns prev(storing the new head) 

EDGE: []
prev is null, curr is the head(null)
loop doesn't run because curr is null
return prev (return null--expected behavior)

EDGE: 1->#
prev is null, curr is head(1)
loop runs since curr is not null
prev is null, curr is 1; save curr.next to temp(null); set curr.next to prev and now 1 points to null still; move prev to curr and now prev is at 1; move curr to temp and now curr is null and loop exits
return prev(1)

EDGE: two nodes, a large list(running out of space); duplicate values;
COMPLEXITY: Time is O(n), Space O(1)


Algorithm 2:
Recursion
In recursion, what you want to do is to break down the list to its smallest sub-problem; one node
Our base case obviously is an empty list so if empty return null
how our loop or recursion is running is, only if the head.next exists(so if its not only one node):
Call the function recursively on the head.next(to break it down to one nodes first)
NOw do the work as you recur back up the stack. Initially our Newhead is pointing at the last node(last recursive call)
so to reverse our links, set the head.next's next pointer to head; then set our head's next pointer to point to none

The reason why we are doing this only if head.next exists is so that we can set head.next's next pointer to head. if head.next doesn't exist, head.next's next pointer doesn't exist as well. and if that's the case(in a list with only a node); then just return the head itself

Test cases:
NORMAL: 1->2->3->4->5
call the function on each node so now the last call ends with newhead as 5
since head.next of 5 doesn't exist, head.next = none 
pop from the stack the previous call so now head = 4; set head.next's next pointer to head(reverse it) and head.next(5.next) is set to none; 5 is still our newhead
pop from the stack the previous call so now head = 3; set head.next's next pointer to head(reverse it)now 4 points at 3; head.next(3.next) is set to none
pop from the stack the previous call so now head = 2; set head.next's next pointer to head(reverse it) now 3 points at 2; head.next(2.next) is set to none
pop from the stack the previous call so now head = 1; set head.next's next pointer to head(reverse it) and now 2 points at 1; head.next(1.next) is set to none
and we are done since all our recursive calls have popped out and return the pointer to newhead=5

EDGE: []
Base case if head is none, return none

EDGE: 1->#
call function on each node and last call ends with newhead as 1(only recursive function)
pop from the stack and now head is 5; since head.next is none, that call to head.next.next doesn't run and you just return the newhead which is just 1

COMPLEXITY: Time: O(n), Space: O(n) the depth of the recursive stack




