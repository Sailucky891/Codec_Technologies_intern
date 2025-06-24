import re

# Predefined patterns and responses
responses = {
    r'hi|hello|hey': "Hello! How can I assist you today?",
    r'what.*(your name|who are you)': "I am your virtual customer assistant 🤖.",
    r'how.*help|what.*can you do': "I can help you with order status, refunds, and general inquiries.",
    r'order status|where.*order': "Please provide your order ID, and I will check the status for you.",
    r'refund|return': "You can initiate a refund or return through your order history page. Do you need the link?",
    r'contact.*support|talk.*agent': "Sure, connecting you to a live agent. Please wait...",
    r'thank you|thanks': "You're welcome! 😊",
    r'bye|goodbye': "Goodbye! Have a great day!"
}

# Default fallback response
fallback = "I'm sorry, I didn't understand that. Could you please rephrase?"

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    return fallback

# ------------------------
# Run chatbot loop
# ------------------------
def run_chatbot():
    print("Customer Service Bot is online! (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        reply = chatbot_response(user_input)
        print(f"Bot: {reply}")

# Start chatbot
if __name__ == "__main__":
    run_chatbot()
