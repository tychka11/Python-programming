a = int(input("value temperature: "))
if a < 0:
    print("freezing")
elif 0 <= a < 20:
    print("cold")
elif 20 <= a < 30:
    print("warm")
else:
    print("hot")
