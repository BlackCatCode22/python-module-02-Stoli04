r = input("Enter the first integer: ")
m = input("Enter the second integer: ")
s = input("Enter the third integer: ")

largest = r

if m > r:
        if m > s:
            largest = m
        else:
            largest = s
else:
        if r > s:
            largest = r
        else:
            largest = s

print("The largest integer is ", largest)
