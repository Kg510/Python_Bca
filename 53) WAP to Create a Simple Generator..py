# Program to Create a Simple Generator:

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Example usage
for num in count_up_to(10):
    print(num)  # Outputs: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")