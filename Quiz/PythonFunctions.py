import math #imports the math library
#Python functions assessment
#javi
#time 8:46 - ??
#PROBLEM 1------------------------------------------------------------------------

def pythagtheorem(a, b): #declare a function
    return math.sqrt((a * a) + (b * b)) #pythag theorem

print(pythagtheorem(3, 4)) #call function

#PROBLEM 2------------------------------------------------------------------------

num = 5

def checksign(num):
    if num < 0:
        print("Negative")
    elif num == 0:
        print("Zero")
    elif num > 0:
        print("Positive")
        
checksign(0)

#PROBLEM 3------------------------------------------------------------------------

def factorial(n):
    SKIBIDIJEREMY = 1
    for i in range(1,n+1):
        SKIBIDIJEREMY*=i
        print("MULTIPLYING BY ", i)
    return SKIBIDIJEREMY

print(factorial(5))

