# Sebastian Santa COP 3502
def encode(passcode):
    code = ""
    for digit in passcode:
        shift = str((int(digit) + 3) % 10)
        code += shift
    return code


def decode(password):
    pass


def main():
    # Menu System
    while True:
        print("Menu")
        print("--------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = int(input("Please enter an option: "))
        # These choices utilize the methods shown above the main
        if choice == 1:
            passcode = input("Please enter your password to encode: ")
            new_passcode = encode(passcode)
            print("Your password has been encoded and stored!")
        if choice == 2:
            password = decode(new_passcode)
            print(f"The encoded password is {new_passcode} and the original password is {password}")
        if choice == 3:
            break


if __name__ == '__main__':
    main()
