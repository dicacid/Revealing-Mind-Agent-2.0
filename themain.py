# Revealing Mind Agent 2.0 – Starter Script

import time

def main():
    print("\n============================")
    print("  🔥 Revealing Mind Agent 2.0 🔥")
    print("============================")
    print("Status: BOOTED SUCCESSFULLY\n")
    
    while True:
        user_input = input("> Enter a command: ").strip().lower()
        if user_input in ("exit", "quit"): 
            print("Shutting down. Peace out.")
            break
        elif user_input == "status":
            print("Agent Status: ✅ Operational")
        else:
            print(f"Unknown command: {user_input}")

if __name__ == "__main__":
    main()
