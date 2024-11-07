def main():
    user_string = input("Enter String: ")
    if user_string == user_string[::-1]:
        print(f"User entered string is a palindrome")
    else:
        print(f"User entered string is not a palindrome")

if __name__ == "__main__":
    main()

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")