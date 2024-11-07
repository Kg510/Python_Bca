# Program to demonstrate try, except, and else

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The result is {result}")


print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")