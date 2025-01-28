#Asks the user for 2 numbers, and will tell which one is greater
x = int(input("Choose a number"))
y = int(input("What is your second number"))
if x > y:
    print("FIRST ONE BIGGER")
elif y > x:
    print("SECOND ONE BIGGER")
else:
    print("Equal.")

#asks the user for a number, and will print QUACK for that number
z = int(input("Choose a number"))
for x in range(x):
    print("Quack")

#Prints a list with 5 people, adds one more, and prints the first and third person
people = ["jeremy", "raidin", "pablo", "noah", "alejandro"]
print("List: ", people)
people.append("kenny")
print("New list: ", people)
print("First and Third persons: ", people[0],people[2])
