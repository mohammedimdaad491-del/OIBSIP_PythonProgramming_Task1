import random
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""
    password_chars = []

    if use_letters:
        character_pool += string.ascii_letters
        password_chars.append(random.choice(string.ascii_letters))

    if use_numbers:
        character_pool += string.digits
        password_chars.append(random.choice(string.digits))

    if use_symbols:
        character_pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    if not character_pool:
        return None

    while len(password_chars) < length:
        password_chars.append(random.choice(character_pool))

    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))

        if length < 1:
            print("Password length must be greater than 0.")
            return

        use_letters = input("Include letters? (y/n): ").lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        selected_types = sum([use_letters, use_numbers, use_symbols])
        if selected_types == 0:
            print("You must select at least one character type.")
            return

        if length < selected_types:
            print(f"Password length must be at least {selected_types} to include all selected character types.")
            return

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print("\nGenerated Password:")
            print(password)
        else:
            print("Error generating password.")

    except ValueError:
        print("Invalid input. Please enter numeric values for length.")


if __name__ == "__main__":
    main()
