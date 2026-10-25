# DATA STRUCTURES EXAMPLES:


# vector 

v = [10,20,30] # creates a list
v.append(40)  # adds an intem at the end of the list
print(v[2]) # prints the item at position 2. The append starts at position 0
v.insert(0,5) # adds the value 5 at position 0, which is the front of the list.

# deque: add or remove at both ends

from collections import deque

d  = deque([10,20,30])
d.appendleft(5) #[5,10,20,30]
d.append(40) # [5,10,20,30,40]
d.popleft() # removes the item at the front of the deque and returns for you

#stack

s = []
s.append(1); s.append(2); s.append(3) # 3 is in the top of the list
print(s[-1]) # 3
s.pop() # removes 3, now 2 is on top


#segment tree, each node stores the sum of a chunk of array, s uou don't have to re-add 
# everything every time someone asks about a range




is 

