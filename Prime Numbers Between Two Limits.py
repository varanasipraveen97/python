lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Prime numbers:")

for n in range(lower, upper + 1):
    if n > 1:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print(n, end=" ")


#Enter lower limit: 12
#Enter upper limit: 56
#Prime numbers:
#13 17 19 23 29 31 37 41 43 47 53 
