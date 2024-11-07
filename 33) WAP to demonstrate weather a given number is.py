def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)

    sum_of_powers = 0

    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits

    if sum_of_powers == number:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")