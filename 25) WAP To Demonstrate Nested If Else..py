# Nested if-else example

myAge = int(input('Enter age: '))

if myAge >= 18:
    myComment = "You can vote."
else:
    if myAge >= 10:
        myComment = "You are in middle school."
    else:
        if myAge >= 6:
            myComment = "You are in primary school."
        else:
            myComment = "You are too small to learn Python"

print("At age: " + str(myAge) + " -> " + myComment)

print("\nThis Program Is Demonstrated By Kunal, ERP:- 0221BCA034")
