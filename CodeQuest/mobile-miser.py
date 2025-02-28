#probably the hardest code quest problem i have done yet
import math
import sys

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

cases = int(input().rstrip())
for i in range(cases):
    #test = "$$$Abc$$$"
    #print(test.rstrip("$"))
    #print(test.lstrip("$"))
    #print(test.strip("$"))
    totalbill = float(input().rstrip().lstrip("$"))
    print(f"Total of the bill: ${totalbill:.02f}")
    print(f"15% = ${(better_round(totalbill*0.15,2)):.02f}")
    print(f"18% = ${(better_round(totalbill*0.18,2)):.02f}")
    print(f"20% = ${(better_round(totalbill*0.20,2)):.02f}")
