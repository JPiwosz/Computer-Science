userstring = input("Enter String   ")
print(userstring)
vowel_count = 0
for character in userstring:
    if character.lower() in "aeiou":
        vowel_count = vowel_count + 1
print("The number of vowels i the string is",vowel_count)

"""
This checks every individual charcter in the user string and checks if it is a vowel
if it is the vowel count increases by 1
"""


    