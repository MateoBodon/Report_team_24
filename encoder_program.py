#Mateo Bodon's File

def decode():
    pass #for my teamate :)

def encoder(password):
    encoded_chars = [str((int(char) + 3) % 10) for char in password]
    return ''.join(encoded_chars)

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            pass #for my teamate :)
        elif choice == 3:
            break

if __name__ == "__main__":
    main()