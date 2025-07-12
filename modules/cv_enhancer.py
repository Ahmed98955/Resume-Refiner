import os
import sys
import time
from utils.gemini_api import ask_gemini
from PyPDF2 import PdfReader
from utils.cv_pdf_formatter import format_cv_to_pdf
from colorama import Fore, Back, Style, init as colorama_init
colorama_init(autoreset=True)

def animated_progress_bar(duration=3, width=32):
    print(Fore.LIGHTCYAN_EX + '\n🤖 Gemini is thinking... Please wait!' + Style.RESET_ALL)
    for i in range(width+1):
        bar = Fore.GREEN + '█'*i + Fore.LIGHTBLACK_EX + '-'*(width-i) + Style.RESET_ALL
        percent = int((i/width)*100)
        sys.stdout.write(f'\r[{bar}] {percent}%')
        sys.stdout.flush()
        time.sleep(duration/width)
    print()

def print_divider():
    print(Fore.CYAN + '\n' + '═'*50 + Style.RESET_ALL)

def ascii_bar(score, max_score=100, width=30):
    filled = int(width * score / max_score)
    if score >= 80:
        color = Fore.GREEN
    elif score >= 50:
        color = Fore.YELLOW
    else:
        color = Fore.RED
    bar = color + '█'*filled + Style.RESET_ALL + Fore.LIGHTBLACK_EX + '-'*(width-filled) + Style.RESET_ALL
    return f'{color}[{bar}{color}] {score}/{max_score}{Style.RESET_ALL}'

def ascii_pie_chart(percent):
    total = 10
    filled = int(round(percent/10))
    pie = (Fore.GREEN + '●'*filled + Fore.LIGHTBLACK_EX + '◯'*(total-filled) + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + '\nSkill Coverage Pie:' + Style.RESET_ALL)
    print('  ' + pie + f'  {percent}%')

def skill_matrix(skills):
    print(Fore.LIGHTBLUE_EX + '\n🧩 Skill Matrix:' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '┌' + '─'*30 + '┬' + '─'*10 + '┐' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '│' + Fore.WHITE + Style.BRIGHT + ' Skill'.ljust(30) + Fore.LIGHTBLACK_EX + '│' + ' Status   ' + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '├' + '─'*30 + '┼' + '─'*10 + '┤' + Style.RESET_ALL)
    for skill, status in skills:
        color = Fore.GREEN if status == 'Strong' else (Fore.YELLOW if status == 'Average' else Fore.RED)
        print(Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL + skill.ljust(30) + Fore.LIGHTBLACK_EX + '│' + color + status.center(9) + Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '└' + '─'*30 + '┴' + '─'*10 + '┘' + Style.RESET_ALL)

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        return text.strip()
    except Exception as e:
        return f"❌ Error reading PDF file: {str(e)}"

import re

def extract_user_info(cv_text):
    """Extracts name, address, phone, email, linkedin from CV text using regex. Returns a dict."""
    info = {}
    # Name: first non-empty line
    lines = [l.strip() for l in cv_text.splitlines() if l.strip()]
    info['name'] = lines[0] if lines else ''
    # Email
    m = re.search(r'[\w\.-]+@[\w\.-]+', cv_text)
    info['email'] = m.group(0) if m else ''
    # Phone
    m = re.search(r'(\+\d{1,3}[- .]?)?(\d{10,15})', cv_text)
    info['phone'] = m.group(0) if m else ''
    # LinkedIn
    m = re.search(r'(linkedin\.com/in/\S+)', cv_text)
    info['linkedin'] = m.group(0) if m else ''
    # Address (look for "Cairo", "Egypt", or similar)
    m = re.search(r'([A-Z][a-z]+,? ?[A-Z][a-z]+)', cv_text)
    info['address'] = m.group(0) if m else ''
    return info

def ask_missing_info(info):
    """Ask user to fill any missing fields in info dict."""
    for field, prompt in [
        ('name', 'Full Name'),
        ('address', 'Address (City, Country)'),
        ('phone', 'Phone Number'),
        ('email', 'Email Address'),
        ('linkedin', 'LinkedIn Profile URL'),
    ]:
        if not info.get(field):
            val = input(f"Please enter your {prompt}: ").strip()
            info[field] = val
    return info

def print_logo_cv_enhancer():
    art = r"""
 ██████╗██╗   ██╗    ███████╗███╗   ██╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
██╔════╝██║   ██║    ██╔════╝████╗  ██║██║  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║    █████╗  ██╔██╗ ██║███████║███████║██╔██╗ ██║██║     █████╗  ██████╔╝
██║     ╚██╗ ██╔╝    ██╔══╝  ██║╚██╗██║██╔══██║██╔══██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗
╚██████╗ ╚████╔╝     ███████╗██║ ╚████║██║  ██║██║  ██║██║ ╚████║╚██████╗███████╗██║  ██║
 ╚═════╝  ╚═══╝      ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝
                                                                                         
"""
    from colorama import Fore, Style
    print(Fore.LIGHTYELLOW_EX + art + Style.RESET_ALL)

def print_divider():
    from colorama import Fore, Style
    print(Fore.MAGENTA + "\n" + "="*60 + Style.RESET_ALL)

def print_choice_bar():
    from colorama import Fore, Style
    print(Fore.GREEN + "\n" + "-"*60 + Style.RESET_ALL)

def enhance_cv():
    print_logo_cv_enhancer()
    from colorama import Fore, Style
    print(Fore.LIGHTYELLOW_EX + "📝 Welcome to the CV Enhancer! Make your CV shine!" + Style.RESET_ALL)
    print_choice_bar()
    print("\n🧠 CV Enhancer Module is running...")
    # Ask for CV path and validate
    while True:
        cv_path = input("📄 Enter your CV file path (PDF or TXT):\n> ").strip()
        if not os.path.exists(cv_path):
            print("❌ File not found. Please enter a valid path.")
        else:
            break
    # Read CV content
    if cv_path.endswith(".pdf"):
        cv_content = extract_text_from_pdf(cv_path)
    else:
        with open(cv_path, "r", encoding="utf-8") as f:
            cv_content = f.read()
    if not cv_content or "❌" in cv_content:
        print(cv_content)
        return
    # Extract user info and ask for missing
    user_info = extract_user_info(cv_content)
    user_info = ask_missing_info(user_info)
    # Prepare Gemini prompt (for enhanced CV)
    prompt = f"""
This is the current CV content:
---
{cv_content}
---
The user's info is:
Full Name: {user_info['name']}
Address: {user_info['address']}
Phone: {user_info['phone']}
Email: {user_info['email']}
LinkedIn: {user_info['linkedin']}
Please rewrite and enhance this CV to make it more professional, clean, and effective. Always include the user's info at the top.
"""
    animated_progress_bar()
    print("\n🔍 Sending CV to Gemini for enhancement...")
    result = ask_gemini(prompt)
    print_divider()
    print(Fore.LIGHTMAGENTA_EX + "🌟 Enhanced CV Analysis 🌟" + Style.RESET_ALL)
    print_divider()
    # Mock score for demo (simulate Gemini giving a score)
    score = 85
    print(Fore.LIGHTBLUE_EX + "\n📈 Enhancement Score:" + Style.RESET_ALL)
    print(ascii_bar(score))
    ascii_pie_chart(score)
    # Mock skill matrix
    skills = [
        ("Professional Formatting", "Strong"),
        ("Contact Info", "Strong"),
        ("Achievements", "Average"),
        ("Clarity", "Strong"),
        ("Grammar", "Strong"),
        ("Design", "Average")
    ]
    skill_matrix(skills)
    print_divider()
    print("\n📄 Preview of the enhanced CV:\n" + (result[:2000] + ("..." if len(result) > 2000 else "")))
    # Ask if user wants to edit the result manually
    while True:
        edit_choice = input("\n✏️ Do you want to edit the enhanced CV manually before saving? (y/n): ").strip().lower()
        if edit_choice in ["y", "n"]:
            break
        print("❌ Invalid input. Please type 'y' or 'n'.")
    if edit_choice == "y":
        import tempfile, subprocess, platform
        with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".txt") as tmp:
            tmp.write(result)
            tmp_path = tmp.name
        print(f"\n🔗 Opening your default text editor for manual editing: {tmp_path}")
        try:
            if platform.system() == "Windows":
                os.startfile(tmp_path)
            elif platform.system() == "Darwin":
                subprocess.call(["open", tmp_path])
            else:
                subprocess.call(["xdg-open", tmp_path])
            input("\nPress Enter after you finish editing and close the editor...")
            with open(tmp_path, "r", encoding="utf-8") as f:
                result = f.read()
        except Exception as e:
            print(f"[ERROR] Could not open editor: {e}")
            print("Proceeding with the original result.")
    # Ask for user approval before saving
    while True:
        approve = input("\n✅ Do you want to save this enhanced CV? (y/n): ").strip().lower()
        if approve in ["y", "n"]:
            break
        print("❌ Invalid input. Please type 'y' or 'n'.")
    if approve == "n":
        print("Operation cancelled. Your CV was not saved.")
        return
    # Choose output format
    while True:
        choice = input("\n💾 Choose output format: [1] TXT or [2] PDF:\n> ").strip()
        if choice in ["1", "2"]:
            break
        print("❌ Invalid choice. Please enter 1 or 2.")
    os.makedirs("outputs", exist_ok=True)
    if choice == "2":
        format_cv_to_pdf(result)
        print("✅ Enhanced CV saved as PDF at: outputs/enhanced_cv.pdf")
    else:
        with open("outputs/enhanced_cv.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("✅ Enhanced CV saved as TXT at: outputs/enhanced_cv.txt")

