# =============================================================
# Project: KendyVerse - KendyTank-Brain
# File: brain02.py
# Version: 0.09 (Status with Disk & Date)
# Date: March 27, 2026
# Developer: Kevin van Rensburg
# =============================================================

import ollama
import shutil  # For disk space
import platform # To check if we are on Windows or Pi
from datetime import datetime

# Direct connection to your local Ollama
client = ollama.Client(host='http://127.0.0.1:11434')

def get_system_stats():
    # 1. Get current Date and Time
    now = datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
    
    # 2. Get Disk Space (C: for Windows, / for Raspberry Pi)
    path = "C:/" if platform.system() == "Windows" else "/"
    total, used, free = shutil.disk_usage(path)
    disk_used_gb = used // (2**30)
    disk_total_gb = total // (2**30)
    
    # 3. Temperature Placeholder (Raspberry Pi real code will go here later)
    temp = "N/A (Windows)" 
    
    print("\n--- [System Status Report] ---")
    print(f"Current Date: {now}")
    print(f"Storage:      {disk_used_gb} GB used of {disk_total_gb} GB")
    print(f"RPi Temp:     {temp}")
    print(f"Device:       {platform.node()} ({platform.system()})")
    print("------------------------------")
    input("\nPress Enter to return to menu...")

def talk_to_ai():
    print("\n--- [KendyAI Mode Active] ---")
    print("(Type 'back' to return to the main menu)")
    system_rules = (
        "You are the Kendy-Brain assistant for the KendyVerse project. "
        "Be friendly, concise, and helpful. Do not mention Alibaba or Qwen."
    )
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'back':
            break
        try:
            print("\n>> ", end="", flush=True)
            stream = client.chat(
                model='qwen2.5:7b',
                messages=[{'role': 'system', 'content': system_rules},
                          {'role': 'user', 'content': user_input}],
                stream=True,
            )
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
            print() 
        except Exception as e:
            print(f"\n[!] Connection Error: {e}")
            break

def tank_controls():
    print("\n--- [KendyTank Manual Override] ---")
    print("Commands: (W) Forward, (S) Backward, (A) Left, (D) Right, (Q) Quit")
    while True:
        cmd = input("\nEnter Command: ").upper().strip()
        if cmd == 'W': print(">> SENT TO UNO: [MOTOR_FORWARD]")
        elif cmd == 'S': print(">> SENT TO UNO: [MOTOR_REVERSE]")
        elif cmd == 'A': print(">> SENT TO UNO: [STEER_LEFT]")
        elif cmd == 'D': print(">> SENT TO UNO: [STEER_RIGHT]")
        elif cmd == 'Q': break
        else: print("[!] Use W, A, S, D or Q.")

def start_brain():
    print("---------------------------------------")
    print("Kendy-Brain: System Online")
    print("---------------------------------------")

    while True:
        print("\n--- Main Menu ---")
        print("1. Talk to KendyAI")
        print("2. Check System Status")
        print("3. Test Tank Movements")
        print("4. Shutdown")
        
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == '1':
            talk_to_ai()
        elif choice == '2':
            get_system_stats()
        elif choice == '3':
            tank_controls()
        elif choice == '4':
            print("\nKendy-Brain: Powering down. Goodbye, Kevin.")
            break
        elif choice == "":
            continue
        else:
            print(f"\n[!] '{choice}' is an invalid selection.")

if __name__ == "__main__":
    start_brain()
