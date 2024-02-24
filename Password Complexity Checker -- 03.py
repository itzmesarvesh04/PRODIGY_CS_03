import re
from colorama import Fore, Style

def check_password_complexity(password):
    has_lowercase = re.search(r"[a-z]", password)
    has_uppercase = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[!@#$%^&*()-+=]", password)
    
    length = len(password)
    
    feedback = {
        "length": length >= 8,
        "lowercase": bool(has_lowercase),
        "uppercase": bool(has_uppercase),
        "digit": bool(has_digit),
        "special": bool(has_special)
    }
    
    score = sum(feedback.values())
    
    if score == 5:
        return f"{Fore.GREEN}Excellent! Your password is very strong.{Style.RESET_ALL}"
    elif score >= 3:
        return f"{Fore.GREEN}Your password is strong.{Style.RESET_ALL}"
    elif score >= 2:
        return f"{Fore.YELLOW}Your password is moderate.{Style.RESET_ALL}"
    elif score >= 1:
        return f"{Fore.RED}Your password is weak.{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Your password is very weak.{Style.RESET_ALL}"

def main():
    
    print(Fore.LIGHTYELLOW_EX + "\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print(Fore.GREEN + "\n       Welcome to Password Complexity Checker!" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-." + Style.RESET_ALL)
    
    while True:
        print("\nPlease choose an option:\n")
        print("1. Check password complexity")
        print("2. Exit")
    
        option = input(Fore.MAGENTA + "\nEnter your choice: ")
    
        if option == "1":
            print("\n" + Fore.BLUE + "Password Complexity Checker" + Style.RESET_ALL)
            print("----------------------------")
            password = input("Enter your password: ")
            complexity_feedback = check_password_complexity(password)
            print("\n" + complexity_feedback + "\n")
            # Write plain text to file without color codes
            with open("verified.txt", "a") as file:
                file.write(f"Password: {password}\nStrength: {complexity_feedback.replace(Fore.GREEN, '').replace(Fore.YELLOW, '').replace(Fore.RED, '').replace(Style.RESET_ALL, '')}\n\n")
        elif option == "2":
            print(Fore.CYAN + "\nExiting the program." + Fore.GREEN + "\nGoodbye!\n")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
if __name__ == "__main__":
    main()
