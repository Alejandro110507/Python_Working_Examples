#The challenge: you are given a number n. For every integer i from 1 to n
# build a label by adding these works in this order, for each rule that applies:

#Fizz if i is divisible by 3 - Result 1
#Buzz if the digit 5 appears in i - Result 2
#Mirror if i has at least 2 digits and reads the same forward and backward - Result 3
#Square if i is a perfect square  - Result 4
#Prime if i is prime - Result 5

#If no rule applies, print i itself. Print one result per line.

print("Hello")
import math

def is_prime(i):
    if i < 2:
        return False  # 1 is neither prime nor composite number
    for d in range(2, i):
        if i % d == 0:
            return False
    return True
    
    
def numberlabels(n):

    for i in range(1,n+1):

        s = str(i)
        label = "" # label is initially empty
        if i % 3 ==0:
            label += "Fizz" # Result 1
        if "5" in s:
            label += "Buzz" # Result 2
        if len(s) >= 2 and s == s[::-1]:
            label += "Mirror" # Result 3
        if math.isqrt(i) **2 == i:
            label += "Square"
        if is_prime(i):
            label += "Prime" # Result 4
        if label == "":
            print(i)
        else: 
            print(label) # apply at least one rule from abovve
        
numberlabels(30)
        
        
        