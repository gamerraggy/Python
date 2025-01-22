#grade calculator: create a function that calculates the final letter grade for a student based on their percentage score
#the function shoulde take a singler argument-the score as a percentage
#and return the correspinding letter grsade base on the following scale:






def gradecalc(percent):
    if percent>=90:
        return "A"
    elif percent>= 80:
        return "B"
    elif percent>=70:
        return "C"
    elif percent>=60:
        return "D"
    else:
        return "F"

print("your grade is,", gradecalc(88))


