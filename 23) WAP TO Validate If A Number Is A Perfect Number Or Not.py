def is_a_perfect_number(n):
    # If the number is less than 2, it cannot be a perfect number.
    if n < 2:
        return False

    divisors_sum = 1
    # Loop through possible divisors from 2 up to the square root of the number.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i

    # Check if the sum of the divisors equals the number itself.
    return divisors_sum == n

# Get user input
number = int(input("Enter a number: "))

# Check if the number is perfect and print the result
if is_a_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")
