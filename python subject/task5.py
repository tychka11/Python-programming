a = int(input("Enter a number between 1 and 7: "))
d = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
print(d.get(a, "error"))