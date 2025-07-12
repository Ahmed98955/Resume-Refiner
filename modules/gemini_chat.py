import os
import requests

def print_logo_gemini():
    art = r"""
 ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗██╗     ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝ ██╔════╝████╗ ████║██║████╗  ██║██║    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██║  ███╗█████╗  ██╔████╔██║██║██╔██╗ ██║██║    ██║     ███████║███████║   ██║   
██║   ██║██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║    ██║     ██╔══██║██╔══██║   ██║   
╚██████╔╝███████╗██║ ╚═╝ ██║██║██║ ╚████║██║    ╚██████╗██║  ██║██║  ██║   ██║   
 ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                 
"""
    from colorama import Fore, Style
    print(Fore.MAGENTA + Style.BRIGHT + art + Style.RESET_ALL)

def gemini_chat():
    print_logo_gemini()
    from colorama import Fore, Style
    print(Fore.MAGENTA + Style.BRIGHT + "✨ Welcome to Gemini Chat! Your AI-powered assistant is ready to help you. ✨" + Style.RESET_ALL)
    print("\n=== Gemini Chat ===")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] Gemini API key not found. Set GEMINI_API_KEY in your environment.")
        return
    print("Type your message to Gemini (type 'exit' to leave chat):")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Gemini chat.")
            break
        prompt = user_input
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
        try:
            resp = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=60)
            if resp.status_code != 200:
                print(f"[Gemini API Error] {resp.status_code}: {resp.text}")
                continue
            data = resp.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            print(f"Gemini: {text.strip()}")
        except Exception as e:
            print(f"[ERROR] {e}")
