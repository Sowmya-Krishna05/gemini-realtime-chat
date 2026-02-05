import os
from memory import ConversationMemory
from gemini_response import generate_response
def main():
    memory = ConversationMemory()

    print("🔹 Gemini Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        answer = generate_response(user_input, memory)
        print("\nGemini:", answer, "\n")


if __name__ == "__main__":
    main()
