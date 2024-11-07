# Program to Use Generator with yield:

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Example usage
for number in countdown(5):
    print(number)  # Outputs: 5, 4, 3, 2, 1


print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")