import math
if a := [int(x) for x in input("numbers: ").split()]:
    print(sum(a), math.fsum(a)/len(a), max(a), min(a))
else:
    print("space")