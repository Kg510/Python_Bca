def reverse_number(number):
    reversed_num = 0
    while number:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return reversed_num

number = int(input("Enter any number: "))
print("Reversed Number:", reverse_number(number))
print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")