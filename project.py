import sys
import string
import secrets
import re

def main():
    display_main_menu()
    option = input()
    match option:
        case "1":
            print(check_password())
        case "2":
            print(generate_password())
        case "3":
            sys.exit()
        case "secret":
            print("You have discovered the secret! Here it is https://youtu.be/yPYZpwSpKmA")
        case _:
            sys.exit("Error, pick a number")


# Function that checks for the basic password stuff like special cases
def check_password():
    display_check_password_menu()
    password_to_check = input()
    if len(password_to_check) <= 0:
        sys.exit("Please enter a password")
    # So ways to check can be length, variety like punctuation or numbers, weak patterns like iiiiii, and common passwords list
    length = len(password_to_check)
    character_label = "Character" if length == 1 else "Characters"
    
    has_uppercase, has_lowercase, has_numbers, has_special_characters = check_variety(password_to_check)
    has_common_password = check_common_password(password_to_check)
    # evaluate the password and return a score and a strength? Or only one is enough?
    strength = calculate_strength(length, has_uppercase, has_lowercase, has_numbers, has_special_characters, has_common_password)

    return f"""
====================================
          Analysis Report
====================================

Length:               {length} {character_label}
Uppercase:            {"Yes" if has_uppercase else "No"}
Lowercase:            {"Yes" if has_lowercase else "No"}          
Numbers:              {"Yes" if has_numbers else "No"}
Special characters:   {"Yes" if has_special_characters else "No"}
Common password:      {"Yes" if has_common_password else "No"}

Strength: {strength}
"""


def get_length_score(length):

    if length < 8:
        return 0
    elif length < 12:
        return 1
    elif length < 16:
        return 2
    elif length < 20:
        return 3
    else:
        return 4

# I think we can work on this and make it better as well instead of just checking one instance of the variety?
def check_variety(password):
    # If password contains uppercase or lowercase or numbers or special characters, reflect it

    has_uppercase = False
    has_lowercase = False
    has_numbers = False
    has_special_characters = False

    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
        if char in string.ascii_lowercase:
            has_lowercase = True
        if char in string.digits:
            has_numbers = True
        if char in string.punctuation:
            has_special_characters = True

    return has_uppercase, has_lowercase, has_numbers, has_special_characters


# Checks if password exists in a list of common passwords
def check_common_password(password):
    # Read from a file a list of top 10K most common passwords
    with open("10k-most-common.txt") as f:
        for common_password in f:
            if password == common_password:
                return True
        return False
    
def calculate_strength(length, has_uppercase, has_lowercase, has_numbers, has_special_characters, has_common_password):
    
    length_score = get_length_score(length)
    score = length_score

    if has_common_password or length < 4:
        return "Very Weak"
    
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_numbers:
        score += 1
    if has_special_characters:
        score += 1

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


def generate_password():
    length, use_upper, use_numbers, use_special_characters = get_password_preferences()

    # Creates a password pool depending on what the user selected
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_numbers:
        pool += string.digits
    if use_special_characters:
        pool += string.punctuation

    password_list = []
    while len(password_list) < length:
        password_list.append(secrets.choice(pool))

    password = "".join(password_list)

    return f"""
====================================
        Generated Password
====================================

Password: {password}

Length: {length}
Includes uppercase: {"Yes" if use_upper else "No"}
Includes numbers: {"Yes" if use_numbers else "No"}
Includes symbols: {"Yes" if use_special_characters else "No"}
"""
    


def get_password_preferences():
    # Prompt user for how many characters they want their password to have
    # Ask them if they want uppercase, numbers or special characters
    # Run the check password strength function once generated
    print("""
====================================
        Generate a Password
====================================
""")
   
    length = get_length()
    include_uppercase = get_true_false("Include uppercase? ")
    include_numbers = get_true_false("Include numbers? ")
    include_special_characters = get_true_false("Include special characters? ")

    return length, include_uppercase, include_numbers, include_special_characters



def get_true_false(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        elif value in ("n", "no"):
            return False

def get_length():
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
    print("""    
====================================
     Password Security Analyzer
====================================

1. Analyze a password
2. Generate a password
3. Exit

Choose an option: """, end="")
    

def display_check_password_menu():
    print("""
====================================
        Password Strength Check
====================================

Enter a password to analyze: """, end="")

if __name__ == "__main__":
    main()