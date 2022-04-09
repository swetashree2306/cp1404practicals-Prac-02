"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # if denominator == 0: # Adding these line 12 and 13 code to the existing code to avoid ZeroDivisionError
    #     denominator = int(input("Please enter the denominator greater then zero: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")

"""
Q:1 When will a ValueError occur?
Ans Whenever the input value provided is not an integer value.

Q:2 When will a ZeroDivisionError occur?
Ans Whenever the denominator value is provided 0.

Q:3 Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans Yes it is possible please refer line no. 12 and 13. if this code is add in the program it will instruct the user 
that the given value is less then zero he should insert value more then 0.
"""