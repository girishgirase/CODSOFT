# We start by importing the random and string modules. These modules will help us generate random characters and work with strings.

import random
import string

# This function takes one argument, length, which specifies the desired length of the generated password.
def generate_password(length):
    # Define character sets
    chars = string.ascii_letters  # Letters (both upper and lower case)
    chars += string.digits  # Digits (0-9)
    chars += string.punctuation  # Special characters
    
    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

# Defining the main Function: The main function is the entry point of our program.
def main():
    # Prompt the user for the desired password length
    # We use a try block to attempt to get the desired password length as input from the user using the input function.
    try:
        length = int(input("Enter the desired password length: "))
    # We wrap it in a try-except block to handle the case where the user enters something that is not a valid integer.
    # If a ValueError occurs (e.g., the user enters a non-integer value), we display an error message and exit the program.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # We check if the entered password length is less than or equal to zero.
    # If it is, we display an error message and exit the program since a valid password length should be a positive number.
    if length <= 0:
        print("Password length should be a positive number.")
        return

    # Generate the password
    # If the input is valid, we call the generate_password function with the specified length to generate the password.
    password = generate_password(length)

    # Finally, we display the generated password on the screen.
    print("Generated Password: ", password)

# This block of code ensures that the main function is executed only if the script is run directly (not imported as a module into another script).
if __name__ == "__main__":
    main()
