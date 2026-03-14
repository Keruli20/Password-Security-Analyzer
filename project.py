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
        case _:
            sys.exit("Error, pick a number")


# Function that checks for the basic password stuff like special cases
def check_password():
    display_check_password_menu()
    password_to_check = input()
    length = check_length(password_to_check)
    # So ways to check can be length, variety like punctuation or numbers, weak patterns like iiiiii, and common passwords list
    has_uppercase, has_lowercase, has_numbers, has_special_characters = check_variety(password_to_check)
    weak_found, weak_pattern = check_weak_patterns(password_to_check)
    # check_common_password(password_to_check)
    # evaluate the password and return a score and a strength? Or only one is enough?

    return f"""
====================================
          Analysis Report
====================================

Length:               {length}
Uppercase:            {"Yes" if has_uppercase else "No"}
Lowercase:            {"Yes" if has_lowercase else "No"}          
Numbers:              {"Yes" if has_numbers else "No"}
Special characters:   {"Yes" if has_special_characters else "No"}
Weak pattern:         {"Yes (" + weak_pattern + ")" if weak_found else "No"}
Common password:      YES / NO

Score: show a score
Strength: show a rating
"""


def check_length(password):

    if len(password) < 8:
        return "Very Weak"
    elif len(password) < 12:
        return "Weak"
    elif len(password) < 16:
        return "Medium"
    elif len(password) < 20:
        return "Strong"
    else:
        return "Very Strong"

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
def check_common_password():
    # Read from a file a list of top 10K most common passwords
    ...

# Uses pattern detection to detect weak passwords
def check_weak_patterns(password):
    repeated =  re.search(r'(.)\1{3,}', password)
    if repeated:
        return True, repeated.group()
    
    sequential_numbers = has_sequential_numbers(password)
    if sequential_numbers:
        return True, sequential_numbers
    
    sequential_letters = has_sequential_letters(password)
    if sequential_letters:
        return True, sequential_letters
   

def has_sequential_numbers(password):
    sequences = ["0123", "1234", "2345", "3456", "4567", "5678", "6789"]
    
    for numbers in sequences:
        if numbers in password:
            return numbers
    return None

def has_sequential_letters(password):
    password = password.lower()
    sequences = ["abcd", "bcde", "cdef", "defg", "efgh", "fghi", "ghij",
                 "hijk", "ijkl", "jklm", "klmn", "lmno", "mnop", "nopq",
                 "opqr", "pqrs", "qrst", "rstu", "stuv", "tuvw", "uvwx",
                 "vwxy", "wxyz"]
    
    for letters in sequences:
        if letters in password:
            return letters
    return None


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
Includes symbols: {"Yes" if use_special_characters else "No"}"""
    


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