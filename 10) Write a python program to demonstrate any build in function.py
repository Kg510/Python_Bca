user_input = input("Enter a list of numbers seperated by spaces")
input_list = user_input.split()

numbers = list(map(int, input_list))
total = sum(numbers)
length = len (numbers)
sorted_numbers = sorted(numbers)
print(f"Orignal list of numbers:{numbers}")
print(f"Sum of numbers:{total}")
print(f"Number of elements:{length}")
print(f"Sorted list of numbers:{sorted_numbers}")

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")