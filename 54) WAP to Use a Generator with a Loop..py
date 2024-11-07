def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci(10):
    print(num)  # Outputs: 0, 1, 1, 2, 3, 5, 8

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")