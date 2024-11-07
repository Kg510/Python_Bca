# Program to Use yield in a Custom Iterator:

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        while self.n > 0:
            yield self.n
            self.n -= 1

# Example usage
for number in Countdown(5):
    print(number)  # Outputs: 5, 4, 3, 2, 1

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")