# String Methods In Python

# 1. capitalize() - Converts the first character to upper case

# 2. count() - Returns the number of times a specified value occurs in a string

# 3. find() - Searches the string for a specified value and returns the position of where it was found

# 4. isalnum() - Returns True if all characters in the string are alphanumeric
# 5. isalpha() - Returns True if all characters in the string are in the alphabet

# 6. isdigit() - Returns True if all characters in the string are digits

# 7. islower() - Returns True if all characters in the string are lower case
# 8. isupper() - Returns True if all characters in the string are upper case


# 9. lower() - Converts a string into lower case
# 10. upper() - Converts a string into upper case

# 11. replace() - Returns a string where a specified value is replaced with a specified value

# Example 1

# capitalize()

Text = "hey, how are you?"
result = Text.capitalize()
print(result)


# Example 2

# count() 

Text = "hey, how are you?"
result = Text.count("e")
print(result)


# Example 3

# find()

Text = "whats up?"
result = Text.find("up")
print(result)



# Example 4

# isalnum()

password = "dummy2025"
result = password.isalnum()
print(result)


# Example 5

# isalpha()

Name = "LalithMohan"
result = Name.isalpha()
print(result)



# Example 6

# isdigit()

phone_number = "1234567890"
result = phone_number.isdigit()
print(result)


# Example 7

# islower()

Text = "hey, how are you?"
result = Text.islower()
print(result)


# Example 8

# isupper()

Text = "HEY, HOW ARE YOU?"
result = Text.isupper()
print(result)


# Example 9

# lower()

Text = "HEY, HOW ARE YOU?"
result = Text.lower()
print(result)


# Example 10

# upper()

Text = "hey, how are you?"
result = Text.upper()
print(result)


# Example 11

# replace()

Name = "Lalithrichard"
result = Name.replace("richard","Mohan")
print(result)



# One Problem Excersice

# Question : write a program get a user name and no more than 10 characters and it must not contain any special spaces and must not contain any numbers

# Solution


User_name = input("Enter your name: ")

if len(User_name) > 10:
    print("please enter a user name with no more than 10 characters")
elif not User_name.isalpha():
    print("please enter a user name with no numbers or special characters")
else:
    print(f"Hello {User_name} ")