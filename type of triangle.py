a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")



#Enter first side: 3
#Enter second side: 5
#Enter third side: 7
#Scalene triangle
