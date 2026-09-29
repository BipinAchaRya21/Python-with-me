# Comparision operators
# a=10
# b=20
# print(a==b) # False 
# print(a!=b)
# print(a>b)
#     =     assignment
#    ==     comparison

# if statement
# age = 22
# if age >=18:
#     print("You are eligible to vote")
 # else statement
    # age1 = 15
    # if age1 >= 18:
        # print("You are an adult")
        
    # else:
        # print("You are a minor")
#elif statement
# marks = int(input("Enter your marks:"))
# if marks >= 80:
#     print("A")
# elif marks >= 60:
#     print("B")
# elif marks >= 40:
#     print("C")
# else:
#     print("Fail")
# Logical Operators : and && Or
# age = 22
# has_id = True
# if age >= 18 and has_id :
#   print("Allowed")
#   day="Sunday"
#   if day=="Sunday" or day=="Saturday":
#     print("Holiday")

# Nested if statement
 
age = 22
has_id = False
if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("Bring your ID")
else: 
    print("You are under 18 kidd!")