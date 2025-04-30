import string
import random
import re

# Function to check password strength
def check_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    if strength == 5:
        remarks = "Very Strong"
    elif strength >= 3:
        remarks = "Strong"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    return strength, remarks

# Function to generate a strong password
def generate_password(length=12):
    if length < 6:
        print("⚠️ Length too short. Minimum 6 characters.")
        return ""
    
    chars = string.ascii_letters + string.digits + "@#$%^&+=!"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Main program
def main():
    print("🔐 Password Tool")
    print("1. Check password strength")
    print("2. Generate strong password")
    choice = input("Choose (1 or 2): ")

    if choice == '1':
        user_pass = input("Enter your password: ")
        strength, remark = check_strength(user_pass)
        print(f"✅ Strength: {strength}/5 → {remark}")
    elif choice == '2':
        length = int(input("Enter desired length: "))
        pwd = generate_password(length)
        print(f"🔑 Generated Password: {pwd}")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
