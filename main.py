import string

password = "helloworld"

upper_case = [1 if c in string.ascii_uppercase else 0 for c in password]

print(string.ascii_uppercase)
