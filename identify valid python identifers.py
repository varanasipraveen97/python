#identifer cannot start with digit
print("2value->invalid")
#identifer Starts with a letter and contains only letters, digits, and an underscore.
print("value_2->valid")
#Identifiers can start with an underscore
print("_hidden->valid")
#class is a Python reserved keyword, so it cannot be used as an identifier.
print("class->invalid")
#Hyphens (-) are not allowed in identifiers; Python treats - as the subtraction operator.
print("my-var->invalid")
#identifer Starts with a letter and uses only letters. This is a valid class name following Python naming conventions
print("MyClass->valid")
#The dollar sign ($) is not allowed in Python identifiers.
print("total$->invalid")

#2value->invalid
#value_2->valid
#_hidden->valid
#class->invalid
#my-var->invalid
#MyClass->valid
#total$->invalid
