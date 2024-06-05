def check_password_strength(password):
    # Initialize variables to track password criteria
    length = len(password)
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    # Define special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>/?`~"

    # Check each character of the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_characters:
            has_special = True

    # Calculate score based on criteria
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1

    # Determine feedback based on score
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

# Test the function
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)


# "🌟 Elevate your career in the digital age! 🌟

# Ready to make bold moves in the ever-evolving world of tech? Let's connect and explore opportunities together. Whether you're a seasoned pro or just starting out, let's navigate this exciting journey together! 🚀 #TechCareer #Networking #Opportunity"

# Feel free to adjust it to fit your specific style or message!