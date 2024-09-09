a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if b > a:
  if b > c:
    largest = b
  else:
    largest = c
else:
  if a > c:
    largest = a
else:
    largest = c


print("The largest number is:", largest)
