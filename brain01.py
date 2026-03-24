# Kendy-Brain v0.02 - The Workshop Menu

def show_menu():
    print("\n--- KENDYVERSE WORKSHOP ---")
    print("1. Check System Status")
    print("2. Connect to Scavenger Tank")
    print("3. Exit Brain")
    
def start_brain():
    print("Kendy-Brain: Online.")
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-3): ")
        
        # Everything below here is indented 8 spaces to stay inside the 'while' loop
        if choice == "1":
            print("\n--- OPENING LOGBOOK ---")
            with open("logbook.txt", "r") as file:
                print(file.read())
        elif choice == "2":
            print("\n[TANK]: Searching for Scavenger connection... (Simulated)")
        elif choice == "3":
            print("\nShutting down. See you in the KendyVerse!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    start_brain()
