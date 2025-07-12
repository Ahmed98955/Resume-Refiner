# modules/job_matcher.py
# 🚀 Super-Enhanced Job Matcher with Graphics, Colors, and Fun! 🚀
import os
import sys
import time
import random
from utils.gemini_api import ask_gemini
from PyPDF2 import PdfReader
from colorama import Fore, Back, Style, init as colorama_init
colorama_init(autoreset=True)

# =========================
# 1. Helper Functions (Global)
# =========================
def animated_progress_bar(duration=3, width=32):
    print(Fore.LIGHTCYAN_EX + '\n🤖 Gemini is thinking... Please wait!' + Style.RESET_ALL)
    for i in range(width+1):
        bar = Fore.GREEN + '█'*i + Fore.LIGHTBLACK_EX + '-'*(width-i) + Style.RESET_ALL
        percent = int((i/width)*100)
        sys.stdout.write(f'\r[{bar}] {percent}%')
        sys.stdout.flush()
        time.sleep(duration/width)
    print()

def extract_score(text):
    import re
    match = re.search(r"match score[:\s]*([0-9]{1,3})/100", text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r"([0-9]{1,3})/100", text)
    if match:
        return int(match.group(1))
    return None

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

def print_divider():
    print(Fore.CYAN + '\n' + '═'*50 + Style.RESET_ALL)

def skill_matrix(skills):
    print(Fore.LIGHTBLUE_EX + '\n🧩 Skill Matrix:' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '┌' + '─'*30 + '┬' + '─'*10 + '┐' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '│' + Fore.WHITE + Style.BRIGHT + ' Skill'.ljust(30) + Fore.LIGHTBLACK_EX + '│' + ' Status   ' + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '├' + '─'*30 + '┼' + '─'*10 + '┤' + Style.RESET_ALL)
    for skill, status in skills:
        color = Fore.GREEN if status == 'Strong' else (Fore.YELLOW if status == 'Average' else Fore.RED)
        print(Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL + skill.ljust(30) + Fore.LIGHTBLACK_EX + '│' + color + status.center(9) + Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '└' + '─'*30 + '┴' + '─'*10 + '┘' + Style.RESET_ALL)

def ascii_pie_chart(percent):
    total = 10
    filled = int(round(percent/10))
    pie = (Fore.GREEN + '●'*filled + Fore.LIGHTBLACK_EX + '◯'*(total-filled) + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + '\nSkill Coverage Pie:' + Style.RESET_ALL)
    print('  ' + pie + f'  {percent}%')

# =========================
# 1. Funky Animated Logo
# =========================
LOGO = f"""
{Fore.CYAN}{Style.BRIGHT}
   ██████╗ ██╗   ██╗      ███╗   ███╗ █████╗ ████████╗ ██████╗  ██████╗ ███████╗
  ██╔═══██╗██║   ██║      ████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██╔════╝
  ██║   ██║██║   ██║█████╗██╔████╔██║███████║   ██║   ██║   ██║██║   ██║███████╗
  ██║   ██║██║   ██║╚════╝██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║   ██║╚════██║
  ╚██████╔╝╚██████╔╝      ██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████║
   ╚═════╝  ╚═════╝       ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{Style.RESET_ALL}
"""

LOGO_TAG = f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}AI CV Matcher v2.0 - with Graphics!{Style.RESET_ALL}"

# Fun animated welcome
WELCOME_LINES = [
    f"{Fore.LIGHTCYAN_EX}Welcome to the most colorful CV-Job Matcher in the universe! 🌈{Style.RESET_ALL}",
    f"{Fore.LIGHTYELLOW_EX}Let's make your job search... less boring! 😎{Style.RESET_ALL}",
    f"{Fore.LIGHTGREEN_EX}Now with graphs, emojis, and a sprinkle of magic! ✨{Style.RESET_ALL}"
]

def animated_logo():
    for line in LOGO.splitlines():
        print(line)
        time.sleep(0.03)
    print(LOGO_TAG)
    for l in WELCOME_LINES:
        print(l)
        time.sleep(0.5)
    print(Fore.CYAN + "═" * 80 + Style.RESET_ALL)
    time.sleep(0.2)

# =========================
# 2. Interactive Main Menu
# =========================
def show_main_menu():
    menu = f"""
{Fore.LIGHTBLUE_EX}{Style.BRIGHT}╔════════════════════════════════════════════════════════════════════╗
║      {Fore.LIGHTMAGENTA_EX}1. Match CV to Job (with Graphics!){Fore.LIGHTBLUE_EX}                ║
║      {Fore.LIGHTMAGENTA_EX}2. Compare Multiple CVs/Jobs{Fore.LIGHTBLUE_EX}                      ║
║      {Fore.LIGHTMAGENTA_EX}3. Show Example Graphs{Fore.LIGHTBLUE_EX}                            ║
║      {Fore.LIGHTMAGENTA_EX}4. Settings & Themes{Fore.LIGHTBLUE_EX}                              ║
║      {Fore.LIGHTMAGENTA_EX}5. Exit{Fore.LIGHTBLUE_EX}                                           ║
╚════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(menu)
    while True:
        choice = input(Fore.CYAN + "Choose an option (1-5): " + Style.RESET_ALL).strip()
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        print(Fore.RED + "❌ Invalid choice. Please enter a number from 1 to 5." + Style.RESET_ALL)

# =========================
# 3. Fun Demo Graphs Section
# =========================
def show_example_graphs():
    print(Fore.YELLOW + Style.BRIGHT + "\n--- Example Graphs & Visuals ---\n" + Style.RESET_ALL)
    # Example: Bar chart
    print(Fore.GREEN + "Match Score Bar:")
    print(Fore.GREEN + "[" + "█"*18 + Fore.LIGHTBLACK_EX + "-"*12 + Fore.GREEN + "] 60/100" + Style.RESET_ALL)
    # Example: Pie chart (ASCII)
    print(Fore.LIGHTMAGENTA_EX + "\nPie Chart (Skills):" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + "  ◯◯◯◯◯◯◯◯◯◯" + Style.RESET_ALL)
    print(Fore.GREEN + "  ●●●●" + Fore.YELLOW + "●●" + Fore.RED + "●●●" + Fore.LIGHTBLACK_EX + "●" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "\nRadar Chart (ASCII):" + Style.RESET_ALL)
    # --- ASCII Radar Chart ---
    print(Fore.LIGHTCYAN_EX + r"      /\\")
    print(r"     /  \\")
    print(r"    /    \\")
    print(r"   /------\\")
    print(r"  /        \\")
    print(r" /__________\\")
    print(Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "\nPress Enter to return to the main menu..." + Style.RESET_ALL)
    input()
    # [Placeholder for future graphs and fun features]

# =========================
# 4. Settings & Themes (Stub)
# =========================
def settings_menu():
    print(Fore.LIGHTMAGENTA_EX + "\nSettings & Themes coming soon!" + Style.RESET_ALL)
    print("(You will be able to customize colors, styles, and more.)")
    time.sleep(1)
    input("Press Enter to return to the main menu...")

# =========================
# 5. Multi-CV/Job Comparison
# =========================
def multi_cv_job_comparison():
    print_divider()
    print(Fore.LIGHTMAGENTA_EX + "🌟 Multi-CV/Job Comparison 🌟" + Style.RESET_ALL)
    print_divider()
    # Get number of CVs
    while True:
        try:
            n = int(input(Fore.CYAN + "How many CVs do you want to compare? (2-5): " + Style.RESET_ALL).strip())
            if 2 <= n <= 5:
                break
            print(Fore.RED + "❌ Please enter a number between 2 and 5." + Style.RESET_ALL)
        except Exception:
            print(Fore.RED + "❌ Invalid input. Enter a number." + Style.RESET_ALL)
    cv_paths = []
    for i in range(n):
        path = input(Fore.YELLOW + f"Enter path to CV #{i+1}: " + Style.RESET_ALL).strip()
        cv_paths.append(path)
    job_desc = input(Fore.LIGHTYELLOW_EX + "Paste the job description to compare against:" + Style.RESET_ALL).strip()
    # For demo: assign random scores
    import random
    scores = [random.randint(50, 99) for _ in range(n)]
    names = [f"CV #{i+1}" for i in range(n)]
    # Horizontal Bar Chart
    print_divider()
    print(Fore.LIGHTBLUE_EX + "\n📊 Match Scores (Bar Chart):" + Style.RESET_ALL)
    max_score = max(scores)
    for name, score in zip(names, scores):
        color = Fore.GREEN if score == max_score else (Fore.YELLOW if score > 70 else Fore.RED)
        bar = color + '█' * (score // 2) + Style.RESET_ALL
        print(f"{name.ljust(8)} {bar} {score}/100")
    # Comparison Table
    print_divider()
    print(Fore.LIGHTCYAN_EX + "\n🔎 Comparison Table:" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '┌' + '─'*10 + '┬' + '─'*10 + '┐' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '│' + Fore.WHITE + Style.BRIGHT + ' CV'.ljust(10) + Fore.LIGHTBLACK_EX + '│' + ' Score   ' + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '├' + '─'*10 + '┼' + '─'*10 + '┤' + Style.RESET_ALL)
    for name, score in zip(names, scores):
        color = Fore.GREEN if score == max_score else (Fore.YELLOW if score > 70 else Fore.RED)
        print(Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL + name.ljust(10) + Fore.LIGHTBLACK_EX + '│' + color + str(score).center(8) + Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + '└' + '─'*10 + '┴' + '─'*10 + '┘' + Style.RESET_ALL)
    # Celebration for winner
    print_divider()
    winner = names[scores.index(max_score)]
    print(Fore.LIGHTGREEN_EX + f"\n🏆 {winner} has the highest match score! 🏆" + Style.RESET_ALL)
    print(Fore.YELLOW + r'''
      ★ ☆ ✦ ✧ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰
    ''' + Style.RESET_ALL)
    print_divider()
    input(Fore.LIGHTYELLOW_EX + "\nPress Enter to return to the main menu..." + Style.RESET_ALL)

# =========================
# 5. Enhanced Main Entrypoint
# =========================
def super_job_matcher():
    animated_logo()
    while True:
        c = show_main_menu()
        if c == "1":
            match_job_with_cv()
            print(Fore.LIGHTCYAN_EX + "\nReturning to main menu..." + Style.RESET_ALL)
            time.sleep(1)
        elif c == "2":
            multi_cv_job_comparison()

        elif c == "3":
            show_example_graphs()
        elif c == "4":
            settings_menu()
        elif c == "5":
            print(Fore.LIGHTMAGENTA_EX + "👋 Goodbye! Stay colorful!" + Style.RESET_ALL)
            sys.exit()

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        return text.strip()
    except Exception as e:
        return f"❌ Could not read PDF file: {str(e)}"

def print_logo_job_matcher():
    art = r"""
     ██╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ 
     ██║██╔═══██╗██╔══██╗    ████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
     ██║██║   ██║██████╔╝    ██╔████╔██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝
██   ██║██║   ██║██╔═══╝     ██║╚██╔╝██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║         ██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                         
"""
    from colorama import Fore, Style
    print(Fore.CYAN + art + Style.RESET_ALL)

def print_divider():
    from colorama import Fore, Style
    print(Fore.MAGENTA + "\n" + "="*60 + Style.RESET_ALL)

def print_choice_bar():
    from colorama import Fore, Style
    print(Fore.GREEN + "\n" + "-"*60 + Style.RESET_ALL)

def match_job_with_cv():
    print_logo_job_matcher()
    from colorama import Fore, Style
    print(Fore.LIGHTCYAN_EX + "🎯 Welcome to the Job Matcher! Find your best fit job now!" + Style.RESET_ALL)
    print_choice_bar()
    print("\n🧠 Job Matching Module is now running...")

    cv_path = input("📄 Enter your CV path (PDF or TXT):\n> ").strip()
    job_desc = input("📝 Paste the job description:\n> ").strip()

    if not os.path.exists(cv_path):
        print("❌ File not found. Please check the path.")
        return

    if cv_path.endswith(".pdf"):
        cv_content = extract_text_from_pdf(cv_path)
    else:
        with open(cv_path, "r", encoding="utf-8") as f:
            cv_content = f.read()

    if not cv_content or "❌" in cv_content:
        print(cv_content)
        return

    prompt = f"""
    You have the following CV:
    ---
    {cv_content}
    ---
    And this job description:
    ---
    {job_desc}
    ---
    Is this CV a good fit for the job? Rate the match from 0 to 100, explain why, and suggest improvements.
    """

    # --- Animated Gemini Progress Bar ---
    import sys
    animated_progress_bar()

    print("\n🔍 Processing with Gemini...")
    result = ask_gemini(prompt)
    print("\n📊 Result:")
    print(result)

    # ===== Graphic Visualization Section =====
    import re
    from colorama import Fore, Style
    def extract_score(text):
        match = re.search(r"match score[:\s]*([0-9]{1,3})/100", text, re.IGNORECASE)
        if match:
            return int(match.group(1))
        match = re.search(r"([0-9]{1,3})/100", text)
        if match:
            return int(match.group(1))
        return None

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

    def print_divider():
        print(Fore.CYAN + '\n' + '═'*50 + Style.RESET_ALL)

    # --- Skill Matrix Table ---
    def skill_matrix(skills):
        print(Fore.LIGHTBLUE_EX + '\n🧩 Skill Matrix:' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + '┌' + '─'*30 + '┬' + '─'*10 + '┐' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + '│' + Fore.WHITE + Style.BRIGHT + ' Skill'.ljust(30) + Fore.LIGHTBLACK_EX + '│' + ' Status   ' + '│' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + '├' + '─'*30 + '┼' + '─'*10 + '┤' + Style.RESET_ALL)
        for skill, status in skills:
            color = Fore.GREEN if status == 'Strong' else (Fore.YELLOW if status == 'Average' else Fore.RED)
            print(Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL + skill.ljust(30) + Fore.LIGHTBLACK_EX + '│' + color + status.center(9) + Fore.LIGHTBLACK_EX + '│' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + '└' + '─'*30 + '┴' + '─'*10 + '┘' + Style.RESET_ALL)

    # --- Pie Chart for Skill Coverage ---
    def ascii_pie_chart(percent):
        total = 10
        filled = int(round(percent/10))
        pie = (Fore.GREEN + '●'*filled + Fore.LIGHTBLACK_EX + '◯'*(total-filled) + Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + '\nSkill Coverage Pie:' + Style.RESET_ALL)
        print('  ' + pie + f'  {percent}%')

    score = extract_score(result)
    print_divider()
    print(Fore.LIGHTMAGENTA_EX + "🌟 CV-Job Match Analysis 🌟" + Style.RESET_ALL)
    print_divider()
    if score is not None:
        print(Fore.LIGHTBLUE_EX + "\n📈 Match Score Graphic:" + Style.RESET_ALL)
        print(ascii_bar(score))
        ascii_pie_chart(score)
    else:
        print(Fore.YELLOW + "\n(No match score detected for graphic)" + Style.RESET_ALL)

    # --- Extract skills for matrix (mock for now) ---
    # In real use, parse result for skills and strengths/weaknesses
    skills = [
        ("Python", "Strong"),
        ("Machine Learning", "Strong"),
        ("Communication", "Average"),
        ("Leadership", "Weak"),
        ("Data Analysis", "Strong"),
        ("Public Speaking", "Weak")
    ]
    skill_matrix(skills)

    # Highlight strengths/weaknesses if present
    print(Fore.LIGHTCYAN_EX + "\n🔑 Key Points" + Style.RESET_ALL)
    lines = result.splitlines()
    strengths = [l for l in lines if 'strength' in l.lower() or 'strong' in l.lower()]
    weaknesses = [l for l in lines if 'weak' in l.lower() or 'improve' in l.lower() or '缺点' in l.lower()]
    if strengths:
        print(Fore.GREEN + "\n✅ Strengths:" + Style.RESET_ALL)
        for s in strengths:
            print(Fore.GREEN + "  • " + s.strip('-• ') + Style.RESET_ALL)
    if weaknesses:
        print(Fore.RED + "\n❌ Weaknesses:" + Style.RESET_ALL)
        for w in weaknesses:
            print(Fore.RED + "  • " + w.strip('-• ') + Style.RESET_ALL)
    if not strengths and not weaknesses:
        print(Fore.LIGHTBLACK_EX + "(No explicit strengths/weaknesses detected.)" + Style.RESET_ALL)
    print_divider()
    print(Fore.LIGHTYELLOW_EX + "\n📝 Full Gemini Analysis:" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + result[:2000] + ("..." if len(result) > 2000 else "") + Style.RESET_ALL)
    print_divider()
    # ===== End Graphic Section =====

    save = input("\n💾 Do you want to save the result to a file? (y/n): ").lower()
    if save == "y":
        os.makedirs("outputs", exist_ok=True)
        with open("outputs/job_match_result.txt", "w", encoding="utf-8") as out:
            out.write(result)
        print("✅ Saved to outputs/job_match_result.txt")
