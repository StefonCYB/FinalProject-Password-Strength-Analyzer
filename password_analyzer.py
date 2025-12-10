# Password Strength Analyzer - Updated

import re

COMMON_PASSWORDS = {
    "123456", "123456789", "password", "pasword123", "qwerty",
    "111111", "123123", "abc123", "welcome"
}


def analyze_password(password: str) -> dict:
    """Analyze a single password and return score, strength, and feedback."""
    score = 0
    feedback = []

    # Very basic check
    if not password:
        return {
            "score": 0,
            "strength": "Invalid",
            "feedback": ["Password cannot be empty."]
        }

    # Common password / blacklist check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is on a common-password list and is extremely unsafe.")
        # Hard-cap the score for common passwords
        return {
            "score": 0,
            "strength": "Very Weak",
            "feedback": feedback
        }

    # Length check
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters for strong security.")

    # Character type checks
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add at least one number.")

    if has_special:
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $).")

    # Basic random bump for variety
    variety_count = sum([has_upper, has_lower, has_digit, has_special])
    if variety_count >= 3 and len(password) >= 12:
        score += 1  # reward strong variety in a long password

    # Strength label based on score
    # Max score here is 7
    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    elif 5 <= score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    if not feedback:
        feedback.append("Excellent password strength. No obvious weaknesses detected.")

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


def interactive_mode() -> None:
    """A CLI loop so a user can test multiple passwords."""
    print("=== Password Strength Analyzer ===")
    print("Type 'quit' to exit.\n")

    while True:
        pwd = input("Enter a password to analyze: ")
        if pwd.lower() == "quit":
            print("Exiting analyzer.")
            break

        result = analyze_password(pwd)

        print("\nPassword Analysis Result")
        print("------------------------")
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']} / 7\n")

        print("Feedback:")
        for item in result["feedback"]:
            print(f"- {item}")
        print("\n")


if __name__ == "__main__":
    interactive_mode()
