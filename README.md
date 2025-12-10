# Final Project - Pass Strength Analyzer

## Overview
My final project is a Python-based security automation tool that evaluates the strength of passwords using common security best practices. It demonstrates how Python can be used to automate basic security checks and provides feedback to the user.

## Features
- Interactive command-line interface (CLI) for analyzing multiple passwords
- Checks length and complexity for example if there is uppercase, lowercase, numerical digits, and special characters.
- Detects common passwords using a small built-in blacklist
- Scoring system that classifies passwords as Very Weak, Weak, Moderate, Strong, or Very Strong
- Gives feedback with suggestions for strengthening weak passwords

## How It Relates to Security Automation
Password quality is a foundaional security control. It is your first line of defense. Organizations rely on automated checks to enforce password policies and reduce the risk of account compromise. My tool simulates a simple automated control by evaluating passwords and generating consistent, repeatbale feedback without manual review.

## How to Run
1. Clone the repsoitory
git clone https://github.com/StefonCYB/FinalProject-Password-Strength-Analyzer.git
cd FinalProject-Password-Strength-Analyzer
2. Run the analyzer with Python 3:
python3 password_analyzer.py
3. Follow the prompt and enter passwords to evaluate. Type quit to exit

Author
Stefon Grey
CYB333 Security Automation - Final Project