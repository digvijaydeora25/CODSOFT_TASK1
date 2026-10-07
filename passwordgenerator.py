import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password 

def get_yes_no(prompt):
    answer = input(prompt).strip().lower()
    return answer == "y"

def main():
    print("===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")
 
    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_digits = get_yes_no("Include numbers? (y/n): ")
    use_symbols = get_yes_no("Include symbols (!@#$...)? (y/n): ")
 
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated password: {password}")
 
 
if __name__ == "__main__":
    main()
 