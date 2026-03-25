# Kendy-Brain v0.02 - The Workshop Menu
# Kevin van Rensburg - March 25, 2026

import datetime

def show_menu():
    print("\n--- KENDYVERSE WORKSHOP ---")
    print("1. Check System Status")
    print("2. Connect to Scavenger Tank")
    print("3. Chat with KendyAI") 
    print("4. Exit Brain")

def kendy_chat():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good morning, Kevin! How is Asunción today?"
    elif 12 <= hour < 18:
        greeting = "Good afternoon! How is work going at the workshop?"
    else:
        greeting = "Good evening! Ready to relax in the KendyVerse?"

    print(f"\n--- KendyAI Active ---")
    print(f"[KendyAI]: {greeting}")
    print("(Type 'back' to return to menu)")

    while True:
        user_input = input("\n[YOU]: ")
        
        if user_input.lower() == "back":
            print("[KendyAI]: Returning to Workshop Menu...")
            break
            
        # --- NEW: SAVE TO MEMORY ---
        with open("kendy_memory.txt", "a") as memory_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            memory_file.write(f"{timestamp} | YOU: {user_input}\n")
        # ---------------------------

        # Simple logic responses
        if "hello" in user_input.lower():
            response = "Greetings! Systems are nominal."
        elif "status" in user_input.lower():
            response = "All sensors reporting healthy. Battery at 85%."
        else:
            response = "I am learning... I've saved that to my memory."
            
        print(f"[KendyAI]: {response}")
        
        # Save Kendy's response too!
        with open("kendy_memory.txt", "a") as memory_file:
            memory_file.write(f"{timestamp} | KendyAI: {response}\n")

def start_brain():
    print("Kendy-Brain: Online.")
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            print("\n--- OPENING LOGBOOK ---")
            # This assumes your logbook.txt is in the same folder
            try:
                with open("logbook.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("[ERROR]: logbook.txt not found.")
                
        elif choice == "2":
            print("\n[TANK]: Searching for Scavenger connection... (Simulated)")
            
        elif choice == "3":
            kendy_chat()    
            
        elif choice == "4":
            print("\nShutting down. See you in the KendyVerse!")
            break        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    start_brain()
