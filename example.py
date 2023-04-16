import os

def clear_screen():
    # Clear screen based on platform
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux, macOS, or Unix
        os.system('clear')

def show_menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Reset")

def reset_ui():
    clear_screen()
    print("Terminal UI reset.")
    show_menu()

def handle_option(option):
    if option == '1':
        print("Option 1 selected.")
    elif option == '2':
        print("Option 2 selected.")
    elif option == '3':
        print("Option 3 selected.")
    elif option == '4':
        reset_ui()
    else:
        print("Invalid option. Please try again.")

def main():
    reset_ui()

    while True:
        user_input = input("Enter your option (1/2/3/4): ")
        handle_option(user_input)

if __name__ == '__main__':
    main()
