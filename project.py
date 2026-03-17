import sys
import string
import secrets
from dataclasses import dataclass


def main():
    display_main_menu()
    option = input()
    match option:
        case "1":
            display_check_password_strength_menu()
            given_password = input()
            password_report = analyze_password(given_password)
            display_analysis_report(password_report)
        case "2":
            generated_password = generate_password()
            display_generated_password(generated_password)
        case "3":
            sys.exit()
        case "secret":
            print(
                "You have discovered the secret! Here it is https://youtu.be/yPYZpwSpKmA"
            )
        case _:
            sys.exit("Please choose a valid option")


@dataclass
class PasswordReport:
    length: int
    strength: str
    has_uppercase: bool
    has_lowercase: bool
    has_numbers: bool
    has_special_characters: bool
    is_common_password: bool


# Function that analyzes the password given and returns a class
def analyze_password(password_to_analyze):

    # Ensure that password is not empty
    if len(password_to_analyze) <= 0:
        sys.exit("Please enter a password")

    length = len(password_to_analyze)

    # Checks for password variety (uppercase, lowercase, numbers, special characters)
    has_uppercase, has_lowercase, has_numbers, has_special_characters = check_variety(
        password_to_analyze
    )

    # Checks if password is a common password
    is_common_password = check_if_common_password(password_to_analyze)

    # Evaluate the strength of the password
    strength = evaluate_strength(
        length,
        has_uppercase,
        has_lowercase,
        has_numbers,
        has_special_characters,
        is_common_password,
    )

    return PasswordReport(
        length=length,
        strength=strength,
        has_uppercase=has_uppercase,
        has_lowercase=has_lowercase,
        has_numbers=has_numbers,
        has_special_characters=has_special_characters,
        is_common_password=is_common_password,
    )


# Function that checks for password variety (uppercase, lowercase, numbers, special characters)
def check_variety(password):

    # Returns True if any instance of a uppercase/lowercase/number/special character was found in the password
    has_uppercase = any(char in string.ascii_uppercase for char in password)
    has_lowercase = any(char in string.ascii_lowercase for char in password)
    has_numbers = any(char in string.digits for char in password)
    has_special_characters = any(char in string.punctuation for char in password)

    return has_uppercase, has_lowercase, has_numbers, has_special_characters


# Function that if the password is in a list of common password
def check_if_common_password(password):

    # Read from a txt file with the top 10K most common passwords
    with open("10k-most-common.txt") as f:
        for common_password in f:
            if password == common_password.strip():
                return True
        return False


# Function that evaluates the strength of the password
def evaluate_strength(
    length,
    has_uppercase,
    has_lowercase,
    has_numbers,
    has_special_characters,
    is_common_password,
):

    length_score = get_length_score(length)
    score = length_score

    # If password is a common password or is shorter than 4 characters, consider it very weak
    if is_common_password or length < 4:
        return "Very Weak"

    # Add a point to the length score if password contains any variety
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_numbers:
        score += 1
    if has_special_characters:
        score += 1

    # Assigns the strength based on the number of points total
    if score <= 1:
        strength = "Very Weak"
    elif score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    elif score <= 7:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength


# Functions that assigns the length score of the password
def get_length_score(length):

    # Very weak score
    if length < 8:
        return 0
    # Weak score
    elif length < 12:
        return 1
    # Medium score
    elif length < 16:
        return 2
    # Strong score
    elif length < 20:
        return 3
    # Very strong score
    else:
        return 4


# Function that generates a password
def generate_password():

    # Gets the preferences of the user for generating the password
    length, has_uppercase, has_numbers, has_special_characters = (
        get_password_preferences()
    )

    # Creates a password pool based on the user's preferences
    pool = string.ascii_lowercase
    if has_uppercase:
        pool += string.ascii_uppercase
    if has_numbers:
        pool += string.digits
    if has_special_characters:
        pool += string.punctuation

    # Creates the password securely and randomly
    generated_password_list = []
    while len(generated_password_list) < length:
        generated_password_list.append(secrets.choice(pool))
    generated_password = "".join(generated_password_list)

    # Returns the generated password
    return generated_password


# Function that gets the users password preferences such as length, uppercase, numbers and special characters
def get_password_preferences():

    print(
        """
====================================
        Generate a Password
====================================
"""
    )

    length = get_password_length()
    include_uppercase = get_true_false("Include uppercase? ")
    include_numbers = get_true_false("Include numbers? ")
    include_special_characters = get_true_false("Include special characters? ")

    return length, include_uppercase, include_numbers, include_special_characters


# Function to prompt the user for yes/no
def get_true_false(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        elif value in ("n", "no"):
            return False


# Function to get and validate the length of a password
def get_password_length():
    while True:
        length = input("Length: ").strip()
        try:
            length = int(length)
            if length <= 0:
                print("Must be a positive number")
                continue
            elif length > 100:
                print("Password length is too long")
                continue
            return length
        except ValueError:
            print("Please enter a whole number.")


def display_main_menu():
    print(
        """    
====================================
     Password Security Analyzer
====================================

1. Analyze a password
2. Generate a password
3. Exit

Choose an option: """,
        end="",
    )


def display_check_password_strength_menu():
    print(
        """
====================================
        Check Password Strength 
====================================

Enter a password to analyze: """,
        end="",
    )


def display_analysis_report(password_report):

    character_label = "Character" if password_report.length == 1 else "Characters"

    print(
        f"""
====================================
            Analysis Report
====================================

Length:               {password_report.length} {character_label}
Uppercase:            {"Yes" if password_report.has_uppercase else "No"}
Lowercase:            {"Yes" if password_report.has_lowercase else "No"}          
Numbers:              {"Yes" if password_report.has_numbers else "No"}
Special characters:   {"Yes" if password_report.has_special_characters else "No"}
Common password:      {"Yes" if password_report.is_common_password else "No"}

Strength: {password_report.strength}"""
    )


def display_generated_password(generated_password):

    # Analyze the password strength of the generated password
    password_report = analyze_password(generated_password)

    character_label = "Character" if password_report.length == 1 else "Characters"

    print(
        f"""
====================================
        Generated Password
====================================

Password: {generated_password}

Length: {password_report.length} {character_label}
Includes uppercase: {"Yes" if password_report.has_uppercase else "No"}
Includes numbers: {"Yes" if password_report.has_numbers else "No"}
Includes symbols: {"Yes" if password_report.has_special_characters else "No"}

Strength: {password_report.strength}
"""
    )


if __name__ == "__main__":
    main()
