# Store first name and last name
first = "jarvis"
last = "break"

# Concatenate into full name
full_name = first + " " + last

# Print in different cases
print("UPPERCASE:", full_name.upper())
print("lowercase:", full_name.lower())
print("Title Case:", full_name.title())

# Print length of full name
print("Length:", len(full_name))

# Print first and last characters
print("First character:", full_name[0])
print("Last character:", full_name[-1])

# Extract first name using slicing (without using the original variable)
first_name = full_name[:full_name.index(" ")]

print("First Name:", first_name)


#UPPERCASE: JARVIS BREAK
#lowercase: jarvis break
#Title Case: Jarvis Break
#Length: 12
#First character: j
#Last character: k
#First Name: jarvis
