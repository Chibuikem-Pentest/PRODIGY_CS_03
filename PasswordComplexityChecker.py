import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $).")

    # Determine password strength
    if score >= 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

if __name__ == "__main__":
    print("This is a Password Complexity Checker!")
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nBelow are suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
