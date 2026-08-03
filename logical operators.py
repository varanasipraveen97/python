# Take percentage and attendance as input
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))

# Check scholarship eligibility
eligible = percentage > 75 and attendance > 90

# Print the result
print("Eligible for scholarship:", eligible)


#Enter percentage: 90
#Enter attendance %: 92
#Eligible for scholarship: True
