import re

def pass_strength(password):
    strength_score = 0
    
    # Length check
    if len(password) >= 8:
        strength_score += 1
    
    # Combined checks for uppercase, lowercase, digits, and special characters
    if re.search(r"[A-Z]", password):
        print("Uppercase check passed.")
        strength_score += 1
    if re.search(r"[a-z]", password):
        print("Lowercase check passed.")
        strength_score += 1
    if re.search(r"\d", password):
        print("Digit check passed.")
        strength_score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Special character check passed.")
        strength_score += 1

    # Common patterns check
    common_patterns = {"password", "123456", "qwerty", "admin"}
    if password.lower() not in common_patterns:
        strength_score += 1

    return strength_score


def password_recommendations(strength_score):
    if strength_score < 3:
        return "Weak password. Please improve for better security."
    elif strength_score < 6:
        return "Moderate password. Consider adding more complexity."
    else:
        return "Strong password! Keep it up!"

def main():
    print("Password Analyzer")
    print("===========================")
    password = input("Enter your password: ")
    strength_score = pass_strength(password)
    print("\nPassword Strength Score:", strength_score)
    print("Recommendation:", password_recommendations(strength_score))

if __name__ == "__main__":
    main()


# Examples :- password, Pass123, Str0ngP@ss, qwerty, Password123, ThisIsAVeryLongPassword123!