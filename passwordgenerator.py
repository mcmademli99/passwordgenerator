import random
import string


def generate_password(length=12, include_special_chars=True):
    """
    Generate a random password.

    :param length: Length of the password (default is 12)
    :param include_special_chars: Boolean indicating if special characters should be included (default is True)
    :return: Generated password as a string
    """
    # Define character sets
    letters_and_digits = string.ascii_letters + string.digits
    special_characters = string.punctuation

    # Choose the character set
    if include_special_chars:
        char_set = letters_and_digits + special_characters
    else:
        char_set = letters_and_digits

    # Generate password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password


if __name__ == "__main__":
    # Get user input for password length and special character inclusion
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and print the password
    password = generate_password(length, include_special_chars)
    print(f"Generated password: {password}")
