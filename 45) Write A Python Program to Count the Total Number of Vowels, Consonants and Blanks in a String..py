def main():
    user_string = input("Enter a string: ")
    vowels = 0
    consonants = 0
    blanks = 0

    for each_character in user_string:
        if each_character in 'aeiouAEIOU':
            vowels += 1
        elif each_character.isalpha():
            consonants += 1
        elif each_character == " ":
            blanks += 1

    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")

if __name__ == "__main__":
    main()

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")