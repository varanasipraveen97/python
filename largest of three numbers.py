a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number:", largest)


#Enter first number: 23
#Enter second number: 34
#Enter third number: 12
#Largest number: 34.0
