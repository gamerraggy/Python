#javi and yanira
#python function review
#EZ NGL
def CirlceCirfumference(a):
    return 2 * 3.14 * a
    
result = CirlceCirfumference(5) #function declaration
print("The cirfumference of circle is:", result) #function result


def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

result = isEven(5)
print (result)

def frog(num2):
    for frog in range(num2):
        print("ribbit")
        
result = frog(5)
