import secrets
import string
import sys

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a random password based on user specifications.
    
    Args:
        length (int): The desired length of the password.
        use_upper (bool): Include uppercase letters (A-Z).
        use_lower (bool): Include lowercase letters (a-z).
        use_digits (bool): Include numbers (0-9).
        use_special (bool): Include special characters (!@#$%^&*).
        
    Returns:
        str: The generated password or an error message.
    """
    characters = ""
    
    # Building the character pool based on user selection
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Error handling if no character types are selected
    if not characters:
        return "Error: You must select at least one character type."

    # Using the 'secrets' module for better security in password generation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def main():
    print("--- Secure Password Generator ---")
    
    try:
        # User Input: Prompt for length
        length_input = input("Enter the desired length of the password: ")
        length = int(length_input)
        
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return

        # Complexity Inputs: Explicitly asking for character types
        upper_choice = input("Include uppercase letters (A-Z)? (y/n): ").lower().strip() == 'y'
        lower_choice = input("Include lowercase letters (a-z)? (y/n): ").lower().strip() == 'y'
        digits_choice = input("Include numbers (0-9)? (y/n): ").lower().strip() == 'y'
        special_choice = input("Include symbols/special characters? (y/n): ").lower().strip() == 'y'

        # Generate Password
        result = generate_password(length, upper_choice, lower_choice, digits_choice, special_choice)
      
        # Display the result
        if result.startswith("Error"):
            print(result)
        else:
            print("\n" + "="*30)
            print(f"Generated Password: {result}")
            print("="*30)
            print("Keep this password safe and do not share it.")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the length.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
