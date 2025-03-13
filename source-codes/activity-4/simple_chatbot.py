# Simple Interactive Chatbot using User-Computer Interaction model

def chatbot():
    print("🤖 Hello! I am ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "bye":
            print("ChatBot: Goodbye! 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hi there! How can I help you today?")
        elif "help" in user_input:
            print("ChatBot: Sure! I can answer simple questions or chat with you.")
        elif "how are you" in user_input:
            print("ChatBot: I'm just code, but thanks for asking! 😄")
        else:
            print("ChatBot: Sorry, I don't understand. Try saying 'help'.")

# Run the chatbot
chatbot()
