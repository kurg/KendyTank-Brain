import datetime

def get_time_greeting():
    """Returns a greeting based on the current hour in Asunción."""
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def chat_with_kendy():
    print("\n--- KendyAI Active ---")
    greeting = get_time_greeting()
    print(f"[KendyAI]: {greeting}, Kevin! How is the workshop today?")
    print("(Type 'back' to return to menu)")

    while True:
        user_input = input("\n[YOU]: ").strip().lower()

        if user_input == "back":
            break
        
        # Simple Logic / Memory Check
        if "unity" in user_input:
            print("[KendyAI]: Oh, the KendyVerse-Unity project! How are the Scavenger and the Old Man doing?")
        elif "pistachio" in user_input:
            print("[KendyAI]: A healthy choice! Best snack in the workshop.")
        else:
            print("[KendyAI]: I am learning... I've saved that to my memory.")

def main_menu():
    while True:
        print("\n--- KENDYVERSE WORKSHOP ---")
        print("1. Check System Status")
        print("2. Connect to Scavenger Tank")
        print("3. Chat with KendyAI")
        print("4. Exit Brain")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            print(f"\n[STATUS]: Systems Green. Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        elif choice == "2":
            print("\n[TANK]: Connecting to KendyTank-Brain...")
        elif choice == "3":
            chat_with_kendy()
        elif choice == "4":
            print("Shutting down... see you at 5 AM, Kevin!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
