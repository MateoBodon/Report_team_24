# Mateo Bodon's File

def encoder(password):
    encoded_chars = [str((int(char) + 3) % 10) for char in password]
    return ''.join(encoded_chars)


# Added decoder function to reverse the encoding process
def decoder(encoded_password):
    decoded_chars = [str((int(char) - 3) % 10) for char in encoded_password]
    return ''.join(decoded_chars)


def main():
    encoded_password = ""  # Added variable to store the encoded password
    while True:
        print(
            "\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")  # Added \n before 'Menu' to match the sample output
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            if encoded_password:  # Added to check if there is an encoded password
                print(f"The encoded password is {encoded_password}, and the original password is "
                      f"{decoder(encoded_password)}.")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
