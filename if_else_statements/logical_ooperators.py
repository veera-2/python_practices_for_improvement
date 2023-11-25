 LOGICAL OPERATORS (and,or,not) = used to check if two or more conditional statement are true

# temp = int(input("What is the temperature outside?: "))

# # AND & OR OPERATORS

# if temp >= 1 and temp <= 30:    # this is how you use the 'and' operator, the two condition must be true or else it will print false.
#     print("the temperature is good today!")
#     print("go outside!")
# elif temp < 1 or temp > 30:      # this is how you use the 'or' operators, atleat one condition must be true or else it print false.
#     print("the temperature is bad today!")
#     print("stay inside!")

# NOT OPERATOR = it inverse any value you give it.

# if not(temp >= 0 and temp <= 30):
#     print("the temperature is good today!")
#     print("go outside!")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is bad today!")
#     print("stay inside!")

# if aplicant has high income AND good credit, eligible for loan

# has_high_income = True  # defining our variable
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# elif has_high_income or has_good_credit:
#     print("Still eligible for loan")
# else:
#     print("Not eligible for a loan")
# print("have a good day!")

# example of the 'not' operator

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
print("Have a good day!")

