import sys
import random

def main():
    display_main_menu()
    option = input()
    match option:
        case "1":
            print("1!")
        case "2":
            generate_password()
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
    length, use_upper, use_lower, use_numbers, use_special_characters = get_password_preferences()
    ...


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
    include_lowercase = get_yes_no("Include lowercase? ")
    include_numbers = get_yes_no("Include numbers? ")
    include_special_characters = get_yes_no("Include special characters? ")


    if not any((include_uppercase, include_lowercase, include_numbers, include_special_characters)):
        print("You must choose at least one character type")
        sys.exit()

    return length, include_uppercase, include_lowercase, include_numbers, include_special_characters



def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        elif value in ("n", "no"):
            return False

 # TODO make sure length can't be too long
def get_length():
    while True:
        length = input("Length: ").strip()
        try:
            length = int(length)
            if length <= 0: 
                print("Length must be a positive number")
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