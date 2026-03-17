import project
import pytest


# Function returns an object with the attributes (length, strength, has_uppercase, has_lowercase, has_numbers, has_special_characters, is_common_password)
def test_analyze_password():

    report = project.analyze_password("password")
    assert report.length == 8
    assert report.strength == "Very Weak"
    assert report.has_uppercase == False
    assert report.has_lowercase == True
    assert report.has_numbers == False
    assert report.has_special_characters == False
    assert report.is_common_password == True

    report = project.analyze_password("notacommonpassword123")
    assert report.length == 21
    assert report.strength == "Strong"
    assert report.has_uppercase == False
    assert report.has_lowercase == True
    assert report.has_numbers == True
    assert report.has_special_characters == False
    assert report.is_common_password == False

    report = project.analyze_password("e.Dt+*)6:J(h%T01")
    assert report.length == 16
    assert report.strength == "Very Strong"
    assert report.has_uppercase == True
    assert report.has_lowercase == True
    assert report.has_numbers == True
    assert report.has_special_characters == True
    assert report.is_common_password == False

    with pytest.raises(ValueError):
        project.analyze_password("")


# Function returns a tuple of (has_uppercase, has_lowercase, has_numbers, has_special_characters)
def test_check_variety():
    assert project.check_variety("password") == (False, True, False, False)
    assert project.check_variety("123456") == (False, False, True, False)
    assert project.check_variety("Password123") == (True, True, True, False)
    assert project.check_variety("}]fQx+z&({D+Pa7l") == (True, True, True, True)


# Function returns True if password is in list of common passwords else returns False
def test_check_if_common_password():
    assert project.check_if_common_password("password") == True
    assert project.check_if_common_password("123456") == True
    assert project.check_if_common_password("orange") == True
    assert project.check_if_common_password("notacommonpassword123") == False


# Function with the parameters (length, has_uppercase, has_lowercase, has_numbers, has_special_characters, is_common_password)
def test_evaluate_strength():
    # Length is less than 4 so will always return very weak
    assert project.evaluate_strength(2, True, True, True, True, False) == "Very Weak"
    # Password is a commmon password and will always return very weak
    assert project.evaluate_strength(20, True, True, True, True, True) == "Very Weak"

    assert project.evaluate_strength(5, False, True, False, False, False) == "Very Weak"
    assert project.evaluate_strength(10, True, True, True, False, False) == "Medium"
    assert project.evaluate_strength(15, True, True, True, True, False) == "Strong"
    assert project.evaluate_strength(20, True, True, True, True, False) == "Very Strong"
    # Currently function uses point system to check and therefore might not take into consideration very long passwords as being more secure
    assert project.evaluate_strength(100, False, False, False, False, False) == "Medium"
    assert project.evaluate_strength(16, True, True, True, True, False) == "Very Strong"


# Function returns the length score of the password
def test_get_length_score():
    assert project.get_length_score(1) == 0
    assert project.get_length_score(8) == 1
    assert project.get_length_score(10) == 1
    assert project.get_length_score(12) == 2
    assert project.get_length_score(14) == 2
    assert project.get_length_score(16) == 3
    assert project.get_length_score(18) == 3
    assert project.get_length_score(20) == 4
    assert project.get_length_score(100) == 4


# Function with the parameters (length, has_uppercase, has_numbers, has_special_characters) and returns a randomly generated password
def test_generate_password():
    test_password = project.generate_password(20, True, True, True)
    assert len(test_password) == 20

    test_password = project.generate_password(16, False, False, False)
    assert len(test_password) == 16
