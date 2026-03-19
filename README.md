# Password Security Analyzer

#### Video Demo: https://youtu.be/ykHycXYauKo

## **What is my project?**

Password Security Analyzer is a command-line (CLI) tool written in Python that allows users to either analyze the strength of an existing password or generate a secure password.

When analyzing a password, the program evaluates several factors such as its length, uppercase or lowercase letters, numbers, and special characters. It then uses these factors to determine and display a strength rating.

When generating a password, the user can specify the desired length and choose which character types to include (uppercase letters, lowercase letters, numbers, and special characters). The program then creates a random, secure password based on these preferences.

***

## **Why did I build it?**

I chose this idea for my CS50 Python final project because I wanted to highlight the importance of creating secure passwords. I have a growing interest in cybersecurity, and weak passwords remain one of the most common ways that accounts and systems are compromised.

By building a password analyzer, my goal is to help users understand the strength of their passwords and identify any weaknesses. In addition, the password generator feature allows users to create secure passwords that can be used to improve their account security.

***

## **Example Output**

### **Analyze a password**
```
====================================
    Password Security Analyzer
====================================

1. Analyze a password
2. Generate a password
3. Exit

Choose an option: 1
```
```
====================================
        Check Password Strength
====================================

Enter a password to analyze: wZjINdL(K-H.v'wF130C
```
```
====================================
            Analysis Report
====================================

Length:               20 Characters
Uppercase:            Yes
Lowercase:            Yes
Numbers:              Yes
Special characters:   Yes
Common password:      No

Strength: Very Strong
```
### **Generate a password**
```
====================================
    Password Security Analyzer
====================================

1. Analyze a password
2. Generate a password
3. Exit

Choose an option: 2
```
```
====================================
        Generate a Password
====================================

Length: 20
Include uppercase? y
Include numbers? y
Include special characters? y
```
```
====================================
        Generated Password
====================================

Password: wZjINdL(K-H.v'wF130C
```