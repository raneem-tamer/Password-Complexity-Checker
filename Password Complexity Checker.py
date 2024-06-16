import re

def check_password_strength(password):
    # Define the criteria
    min_length = 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Initialize feedback list
    feedback = []

    # Check each criterion
    if len(password) < min_length:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if not upper:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit:
        feedback.append("Password should include at least one number.")
    if not special:
        feedback.append("Password should include at least one special character.")

    # Assess strength
    if len(feedback) == 0:
        strength = "Strong"
        feedback.append("Your password is strong.")
    elif len(feedback) == 1:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


# Strong password example
password1 = "StrongPass123!"
strength1, feedback1 = check_password_strength(password1)
print(f"Password: {password1}")
print(f"Password strength: {strength1}")
for item in feedback1:
    print(f"- {item}")
print("\n")

# Moderate password example
password2 = "Pass1234"
strength2, feedback2 = check_password_strength(password2)
print(f"Password: {password2}")
print(f"Password strength: {strength2}")
for item in feedback2:
    print(f"- {item}")
print("\n")

# Weak password example
password3 = "weakpass"
strength3, feedback3 = check_password_strength(password3)
print(f"Password: {password3}")
print(f"Password strength: {strength3}")
for item in feedback3:
    print(f"- {item}")