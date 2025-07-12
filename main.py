import os
from colorama import Fore, Style, init as colorama_init
colorama_init()

def print_banner(text):
    print(Fore.CYAN + "\n" + "*" * 60)
    print(f"{text.center(60)}")
    print("*" * 60 + Style.RESET_ALL)

def main():
    print_banner("""
 █████╗ ██╗         ██╗ ██████╗ ██████╗      █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗
██╔══██╗██║         ██║██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝
███████║██║         ██║██║   ██║██████╔╝    ███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║   
██╔══██║██║    ██   ██║██║   ██║██╔══██╗    ██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║   
██║  ██║██║    ╚█████╔╝╚██████╔╝██████╔╝    ██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝     ╚════╝  ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                   
""")
    while True:
        print("\n==== AI Job Assistant ====")
        print("1. CV Enhancer")
        print("2. Job Matcher")
        print("3. Gemini Chat")
        print("4. Exit")
        choice = input("Choose (1–4): ").strip()

        if choice == "1":
            from modules.cv_enhancer import enhance_cv
            enhance_cv()
        elif choice == "2":
            from modules.job_matcher import match_job_with_cv
            match_job_with_cv()
        elif choice == "3":
            from modules.gemini_chat import gemini_chat
            gemini_chat()
        elif choice == "4":
            print(Fore.YELLOW + "👋 Done. Exiting." + Style.RESET_ALL)
            exit()
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()