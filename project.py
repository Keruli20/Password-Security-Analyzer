import sys
import random
import string
import secrets

def main():
    display_main_menu()
    option = input()
    match option:
        case "1":
            print("1!")
        case "2":
            print(generate_password())
        case "3":
            sys.exit()
        case _:
            sys.exit("Error, pick a number")




# Function that checks for the basic password stuff like special cases
def function_1():
    ...


# Checks if password exists in a list of common passwords
def function_2():
    ...

# Uses pattern detection to detect weak passwords
def function_n():
    ...

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
    include_uppercase = get_yes_no("Include uppercase? ")
    include_numbers = get_yes_no("Include numbers? ")
    include_special_characters = get_yes_no("Include special characters? ")

    return length, include_uppercase, include_numbers, include_special_characters



def get_yes_no(prompt):
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

if __name__ == "__main__":
    main()