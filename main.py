import string

password = "helloworld"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_characters = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special_characters, digits]

length = len(password)

score = 0

with open("common_passwords.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score: 0/7")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
if length > 20:
    score += 1
print(f"Password length is {str(length)}, adding {str(score)} points!")
