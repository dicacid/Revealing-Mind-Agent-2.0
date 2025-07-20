# Revealing Mind Agent 2.0 – Local Model Stub

import os

# Placeholder chat function for offline or local models
# You can integrate any local LLM or custom logic here

def chat(prompt: str) -> str:
    # Example stub response; replace with actual model inference
    return f"[Offline Agent] You said: '{prompt}'"


def main():
    print("\n============================")
    print("  🔥 Revealing Mind Agent 2.0 🔥")
    print("============================")
    print("Status: BOOTED SUCCESSFULLY\n")

    # In CI environments (like GitHub Actions), skip interactive loop
    if os.environ.get("CI"):
        print("Running in CI mode – skipping input loop.")
        return

    # Interactive command loop
    while True:
        try:
            user_input = input("> Enter a command: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                print("Shutting down. Peace out.")
                break
            elif user_input.lower() == "status":
                print("Agent Status: ✅ Operational")
            else:
                # Call the chat stub (or replace with real model call)
                response = chat(user_input)
                print(f"\n🤖 Agent Response:\n{response}\n")
        except EOFError:
            print("\nEOF detected. Exiting.")
            break

if __name__ == "__main__":
    main()
