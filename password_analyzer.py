import re

def analyze_password(password: str) -> dict:
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback if feedback else ["Excellent password strength."]
    }


if __name__ == "__main__":
    user_password = input("Enter a password to analyze: ")
    result = analyze_password(user_password)

    print("\nPassword Analysis Result")
    print("------------------------")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}/6")

    print("\nFeedback:")
    for item in result["feedback"]:
        print(f"- {item}")
