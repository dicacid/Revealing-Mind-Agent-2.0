# Revealing Mind Agent 2.0 – Headless-Friendly Mode

import os

def main():
    print("\n============================")
    print("  🔥 Revealing Mind Agent 2.0 🔥")
    print("============================")
    print("Status: BOOTED SUCCESSFULLY\n")

    if os.environ.get("CI"):  # GitHub Actions environment
        print("Running in CI mode – skipping input loop.")
        return

    while True:
        try:
            user_input = input("> Enter a command: ").strip().lower()
            if user_input in ("exit", "quit"): 
                print("Shutting down. Peace out.")
                break
            elif user_input == "status":
                print("Agent Status: ✅ Operational")
            else:
                print(f"Unknown command: {user_input}")
        except EOFError:
            print("\nEOF received – exiting.")
            break

if __name__ == "__main__":
    main()
