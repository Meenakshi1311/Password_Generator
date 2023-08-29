import random
import string


def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return "No characters selected for the password."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter desired password length: "))
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
use_digits = input("Include digits? (yes/no): ").lower() == "yes"
use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

for _ in range(num_passwords):
    password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print("Generated Password:", password)
